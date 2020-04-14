from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from SERVER.models.db.profile import Profile, Chat
from SERVER.models.db.post import Post, Commentary, Like
from SERVER.models.forms.post import PostForm, CommentaryForm, ChatForm, AutocompleteForm
from SERVER.models.db.mission import Result, Mission
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q


def profile(request, userId):

    user = User.objects.get(id=userId)
    userRequest = request.user

    if user.is_authenticated and userRequest.is_authenticated:
        # form post
        Postform = PostForm()
        # autcomlete search navbar post
        Autocompleteform = AutocompleteForm()

        # list users (pas opti)
        users = User.objects.all()
        usersCount = users.count()-1


        #  user
        profile = Profile.objects.get(user_id=userId)
        # list friends user
        friends = profile.friends.all()
        # list follow user
        followers = Profile.objects.filter(friends=user)
        # list posts user
        posts = Post.objects.filter(description=False, author=profile)
        # xp user
        xp = 0
        for commentary in Commentary.objects.filter(description=True, author=profile):
            if commentary.mission.description == True:
                xp = xp + commentary.price
        # average mark user
        averageMark = 0
        averageMarkSize = 0
        for commentary in Commentary.objects.filter(description=True, author=profile):
            if commentary.mission.description == True:
                averageMarkSize = + 1
                averageMark = averageMark + commentary.mission.result.mark
        if averageMarkSize != 0:
            averageMark = averageMark / averageMarkSize
        # Commentary with mission dev
        commentaryMissionDevRequest = Commentary.objects.filter(description=True, author=profile)
        # posts with mission
        postsMissionRequest = Post.objects.filter(description=True, author=profile)


        # view on the other user
        if (userId != request.user.id):

            # form commentary
            Commentaryform = CommentaryForm()
            # form chat
            Chatform = ChatForm()

            # users Count
            usersCount = users.count() - 2

            # chats request/user
            chats = Chat.objects.filter(
                (Q(sender=request.user.profile) & Q(receiver=user.profile))
                | (Q(sender=user.profile) & Q(receiver=request.user.profile)))
            chats = chats.order_by('date')

            # list of my likes on the profile user (pas opti)
            likesRequest = Like.objects.filter(author=request.user.profile)
            postsUserLikedRequest = []
            for likes in likesRequest:
                if posts:
                    if likes.post in posts:
                        postsUserLikedRequest.append(likes.post)

            return render(request, "profile/index.html",
                          {"Postform": Postform,
                           "Autocompleteform":Autocompleteform,
                           "Commentaryform": Commentaryform,
                           "Chatform" : Chatform,
                           "users": users,
                           "usersCount": usersCount,
                           "user": user,
                           "friends": friends,
                           "posts": posts,
                           "chats": chats,
                           "postsUserLikedRequest": postsUserLikedRequest,
                           "commentaryMissionDevRequest": commentaryMissionDevRequest,
                           "postsMissionRequest":postsMissionRequest,
                           "averageMark":averageMark,
                           "xp": xp,
                           "followers": followers
                           })

        return render(request, "profile/index.html",
                      {"Postform": Postform,
                       "Autocompleteform":Autocompleteform,
                       "users": users,
                       "usersCount": usersCount,
                       "user": user,
                       "friends": friends,
                       "posts": posts,
                       "commentaryMissionDevRequest": commentaryMissionDevRequest,
                       "postsMissionRequest": postsMissionRequest,
                       "averageMark": averageMark,
                       "xp": xp,
                       "followers": followers
                       })


def profileSearch(request):
    if request.method == 'POST':
        Autocompleteform = AutocompleteForm(request.POST)
        if Autocompleteform.is_valid():
            username = Autocompleteform.cleaned_data.get('search')
            user = User.objects.get(username=username)
            userId = user.id
    return redirect('profile', userId)


def invite(request, userId):
    if request.method == 'POST':
        profile = Profile.objects.get(user_id=request.user.id)
        friend = User.objects.get(id=userId)
        profile.friends.add(friend)
    return redirect('profile',userId)


@csrf_protect
def autocomplete(request, userId):
    if request.method == 'POST':
        target = request.POST.get('target')
        users = User.objects.filter(username__contains=target)
        listUser = []
        for user in users:
            listUser.append(user.username)
        return HttpResponse(
            json.dumps({"listUser" : listUser}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_protect
def chat(request, userId):
    if request.method == 'POST':
        chat_text = request.POST.get('chat_text')
        user = User.objects.get(id=userId)
        chat = Chat(text=chat_text, receiver=user.profile, sender=request.user.profile)
        chat.save()
        return HttpResponse(
            json.dumps({"chatText": chat.text,
                        "chatReceiver": chat.receiver.user.username,
                        "chatSender": chat.sender.user.username,
                        "chatDate": str(chat.date),
                        }),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_protect
def chats(request, userId):
    if request.method == 'POST':
        chats = Chat.objects.filter(receiver=request.user.profile).order_by('-date')
        listChat = []
        listUsername = []
        listUrl = []
        listDate = []
        for chat in chats:
            if chat.sender.user.username not in listUsername:
                listChat.append(chat.text)
                listUsername.append(chat.sender.user.username)
                listDate.append(str(chat.date))
                if chat.sender.picture.name != False:
                    listUrl.append("/static/media/" + chat.sender.picture.url)


        return HttpResponse(
            json.dumps({"listChat": listChat,
                        "listUsername": listUsername,
                        "listUrl" : listUrl,
                        "listDate": listDate,
                        }),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

