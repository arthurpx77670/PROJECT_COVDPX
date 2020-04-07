from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from SERVER.models.db.db_profil import Profil, Post, Commentary, Like, Chat, Mission
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
    # pas opti
    likesRequest = request.user.profil.like_set.all()
    postsLikedRequest = []
    for likes in likesRequest:
        if posts:
            if likes.post in posts:
                postsLikedRequest.append(likes.post)

    # count files user
    countFiles =0
    for post in posts:
        if post.file != "False":
            countFiles += 1

    # count post research user
    countPosts = 0
    for post in posts:
        if post.description == "Research":
            countPosts += 1

    # all chats bettwen a couple users
    chats = Chat.objects.filter(
        (Q(sender=request.user.profil) & Q(receiver=user.profil))
        |(Q(sender=user.profil) & Q(receiver=request.user.profil)))
    chats = chats.order_by('-date')

    # mission request to dev
    # pas opti
    missionsDevRequest = []
    for mission in Mission.objects.all():
        if(mission.accept.author.user == request.user):
            missionsDevRequest.append(mission)

    # mission request
    # pas opti
    missionsRequest = []
    for mission in Mission.objects.all():
        if (mission.proposition.author.user == request.user):
            missionsRequest.append(mission)

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
                   "countPosts": countPosts,
                   "chats": chats,
                   "missionsDevRequest": missionsDevRequest,
                   "missionsRequest":missionsRequest,
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
            post = Post.objects.get(id=postId)
            author = Profil.objects.get(user=request.user)

            text = Commentaryform.cleaned_data.get('text')
            price = Commentaryform.cleaned_data.get('price')
            commentary = Commentary.objects.create(text=text, author_id=author.id, post_id=postId, price=price)
            commentary.save()


    return redirect('profil',userId)


def post(request, userId):
    if request.method == 'POST':
        Postform = PostForm(request.POST, request.FILES)
        if Postform.is_valid():
            title = Postform.cleaned_data.get('title')
            text = Postform.cleaned_data.get('text')
            price = Postform.cleaned_data.get('price')
            deadline = Postform.cleaned_data.get('deadline')
            if Postform.cleaned_data.get('file') is None:
                file = False
            else:
                file = Postform.cleaned_data.get('file')
            author = Profil.objects.get(user=request.user)
            post = Post.objects.create(title=title, text=text, author_id=author.id, file=file, price=price, deadline=deadline,description="Research")
            post.save()
    return redirect('profil', userId)


def like(request, postId, userId):
    if request.method == 'POST':
        author = Profil.objects.get(user_id=request.user.id)
        like = Like.objects.create(author_id=author.id, post_id=postId)
        like.save()
    return redirect('profil',userId)


def accept(request, userId, postId, commentaryId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        commentary = Commentary.objects.get(id=commentaryId)

        mission = Mission.objects.create(proposition=post, accept=commentary)
        mission.save()

        post.description = "Dev"
        post.save()
    return redirect('profil',userId)


def editPost(request, userId, postId):
    post = Post.objects.get(id=postId)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            price = form.cleaned_data["price"]
            deadline = form.cleaned_data["deadline"]
            if form.cleaned_data.get('file') is None:
                file = False
            else:
                file = form.cleaned_data.get('file')

            post.title = title
            post.text = text
            post.file = file
            post.price = price
            post.file = file
            post.deadline = deadline
            post.save()

            return redirect('profil', userId)
    else:
        if(post.file != 'False'):
            form = PostForm(initial={'title': post.title,
                                     'text': post.text,
                                     'file': post.file,
                                     'price': post.price,
                                     'deadline': post.deadline})
        else:
            form = PostForm(initial={'title': post.title,
                                     'text': post.text,
                                     'price': post.price,
                                     'deadline': post.deadline})

    return render(request, 'profil/internal/profil_edit_post.html', {'form': form})


def deletePost(request, userId, postId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        post.delete()
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

