from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from COVDPX.models.db.db_profil import Profil, Post, Commentary, Like
from COVDPX.models.forms.forms_profil import PostForm, CommentaryForm
from django.http import HttpResponse


def profil(request, userId):

    # form post
    Postform = PostForm()

    # form commentary
    Commentaryform = CommentaryForm()

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

    return render(request, "profil/profil_index.html",
                  {"user": user,
                   "users": users,
                   "friends": friends,
                   "posts": posts,
                   "Postform": Postform,
                   "Commentaryform": Commentaryform,
                   "postsLikedRequest": postsLikedRequest,
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
        Postform = PostForm(request.POST)
        if Postform.is_valid():
            title = Postform.cleaned_data.get('title')
            text = Postform.cleaned_data.get('text')
            author = Profil.objects.get(user=request.user)
            post = Post.objects.create(title=title, text=text, author_id=author.id)
            post.save()

    return redirect('profil', userId)


def like(request, postId, userId):
    if request.method == 'POST':
        author = Profil.objects.get(user_id=request.user.id)
        like = Like.objects.create(author_id=author.id, post_id=postId)
        like.save()
    return redirect('profil',userId)