from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from SERVER.models.db.db_profil import Profil, Post, Commentary, Like, Chat
from SERVER.models.forms.forms_profil import PostForm, CommentaryForm, ChatForm
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

def profil(request, userId):

    # form post
    Postform = PostForm()

    # form commentary
    Commentaryform = CommentaryForm()

    # form chat
    Chatform = ChatForm()

    # page user
    user = User.objects.get(id=userId)
    profil = Profil.objects.get(user_id=userId)

    # list users
    users = User.objects.all()

    # list friends
    friends = profil.friends.all()

    # list posts
    posts = profil.post_set.all()

    # list of my likes on the profil user
    likesRequest = request.user.profil.like_set.all()
    postsLikedRequest = []
    for likes in likesRequest:
        if likes.post in profil.post_set.all():
            postsLikedRequest.append(likes.post)

    # count files user
    countFiles =0
    for post in posts:
        if post.file != "False":
            countFiles += 1

    # all chats bettwen a couple users

    chats = Chat.objects.filter(
        (Q(sender=request.user.profil) & Q(receiver=user.profil))
        |(Q(sender=user.profil) & Q(receiver=request.user.profil)))
    chats = chats.order_by('-date')

    return render(request, "profil/profil_index.html",
                  {"user": user,
                   "users": users,
                   "friends": friends,
                   "posts": posts,
                   "Postform": Postform,
                   "Commentaryform": Commentaryform,
                   "Chatform" : ChatForm,
                   "postsLikedRequest": postsLikedRequest,
                   "countFiles": countFiles,
                   "chats": chats,
                   })


def invitation(request, userId):
    if request.method == 'POST':
        profil = Profil.objects.get(user_id=request.user.id)
        friend = User.objects.get(id=userId)
        profil.friends.add(friend)
    return redirect('profil',userId)


def commentary(request, postId, userId):
    if request.method == 'POST':
        Commentaryform = CommentaryForm(request.POST)
        if Commentaryform.is_valid():
            text = Commentaryform.cleaned_data.get('text')
            author = Profil.objects.get(user=request.user)
            commentary = Commentary.objects.create(text=text, author_id=author.id, post_id=postId)
            commentary.save()

    return redirect('profil',userId)


def post(request, userId):
    if request.method == 'POST':
        Postform = PostForm(request.POST, request.FILES)
        if Postform.is_valid():
            title = Postform.cleaned_data.get('title')
            text = Postform.cleaned_data.get('text')
            file = Postform.cleaned_data.get('file')
            author = Profil.objects.get(user=request.user)
            post = Post.objects.create(title=title, text=text, author_id=author.id, file=file)
            post.save()
    return redirect('profil', userId)


def like(request, postId, userId):
    if request.method == 'POST':
        author = Profil.objects.get(user_id=request.user.id)
        like = Like.objects.create(author_id=author.id, post_id=postId)
        like.save()
    return redirect('profil',userId)


@csrf_protect
def create_chat(request, userId):
    if request.method == 'POST':
        chat_text = request.POST.get('chat_text')

        user = User.objects.get(id=userId)
        chat = Chat(text=chat_text, receiver=user.profil, sender=request.user.profil)
        chat.save()

        return HttpResponse(
            json.dumps({"chatText" : chat.text,
                        "chatReceiver": chat.receiver.user.username,
                        "chatSender": chat.sender.user.username,
                        "chatDate": chat.date,
                        }),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



# @csrf_protect
# def refresh_chat(request, userId):
#     if request.method == 'POST':
#         user = User.objects.get(id=userId)
#         lastChat = request.POST.get('lastChat')
#
#         chats = Chat.objects.filter(
#             (Q(sender=request.user.profil) & Q(receiver=user.profil))
#             | (Q(sender=user.profil) & Q(receiver=request.user.profil)))
#         chats = chats.order_by('-date')
#         user = User.objects.get(id=userId)
#         chats = Chat.objects.filter()
#
#         return HttpResponse(
#             # json.dumps({"chatText": chat.text,
#             #             "chatReceiver": chat.receiver.user.username,
#             #             "chatSender": chat.sender.user.username,
#             #             "chatDate": chat.date,
#             #             }),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

