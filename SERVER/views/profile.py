from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from SERVER.models.db.profile import Profile, Chat
from SERVER.models.db.post import Post, Commentary, Like
from SERVER.models.forms.post import PostForm, CommentaryForm, ChatForm
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

        # list users (pas opti)
        users = User.objects.all()
        usersCount = users.count()-1

        #  user
        profile = Profile.objects.get(user_id=userId)
        # list friends user
        friends = profile.friends.all()
        # list posts user
        posts = Post.objects.filter(description=False, author=profile)

        # request
        profileRequest = Profile.objects.get(user_id=userRequest)
        # Commentary with mission dev request
        commentaryMissionDevRequest = Commentary.objects.filter(description=True, author=profileRequest)

        # posts with mission request
        postsMissionRequest = Post.objects.filter(description=True, author=profileRequest)

        xp = 0
        xpSize = 0
        for commentary in Commentary.objects.filter(description=True, author=profile):
            if commentary.mission.description == True:
                xpSize = + 1
                xp = xp + commentary.price
        if xpSize != 0:
            xp = xp / xpSize


        # average mark user
        averageMark = 0
        averageMarkSize = 0
        for commentary in Commentary.objects.filter(description=True, author=profile):
            if commentary.mission.description == True:
                averageMarkSize =+ 1
                averageMark = averageMark + commentary.mission.result.mark
        if averageMarkSize !=0:
            averageMark = averageMark/averageMarkSize

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
            chats = chats.order_by('-date')

            # list of my likes on the profile user (pas opti)
            likesRequest = Like.objects.filter(author=profileRequest)
            postsUserLikedRequest = []
            for likes in likesRequest:
                if posts:
                    if likes.post in posts:
                        postsUserLikedRequest.append(likes.post)

            return render(request, "profile/index.html",
                          {"Postform": Postform,
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
                           "xp":xp
                           })

        return render(request, "profile/index.html",
                      {"Postform": Postform,
                       "users": users,
                       "usersCount": usersCount,
                       "user": user,
                       "friends": friends,
                       "posts": posts,
                       "commentaryMissionDevRequest": commentaryMissionDevRequest,
                       "postsMissionRequest":postsMissionRequest,
                       "averageMark":averageMark,
                       "xp":xp
                       })


def invite(request, userId):
    if request.method == 'POST':
        profile = Profile.objects.get(user_id=request.user.id)
        friend = User.objects.get(id=userId)
        profile.friends.add(friend)
    return redirect('profile',userId)


@csrf_protect
def chat(request, userId):
    if request.method == 'POST':
        chat_text = request.POST.get('chat_text')

        user = User.objects.get(id=userId)
        chat = Chat(text=chat_text, receiver=user.profile, sender=request.user.profile)
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
#             (Q(sender=request.user.profile) & Q(receiver=user.profile))
#             | (Q(sender=user.profile) & Q(receiver=request.user.profile)))
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

