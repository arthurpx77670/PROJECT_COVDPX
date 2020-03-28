from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from COVDPX.models.db.db_profil import Profil, Post, Commentary
from COVDPX.models.forms.form_profil import PostForm, CommentaryForm
from django.http import HttpResponse


def profil(request, userId):

    # page user
    user = User.objects.get(id=userId)

    # list users
    users = User.objects.all()

    # list friends
    profil = Profil.objects.get(user_id=userId)
    friends = profil.friends.all()

    # list posts
    posts = Post.objects.filter(author_id=userId)

    # commentaries = Commentary.objects.filter(post_id=pot)

    # form post
    Postform = PostForm()

    # form commentary
    Commentaryform = CommentaryForm()

    return render(request, "profil/profil_index.html",
                  {"user": user, "users": users, "friends": friends, "Postform": Postform, "posts": posts, "Commentaryform": Commentaryform})


def invitation(request, userId):

    profil = Profil.objects.get(user_id=request.user.id)
    friend = User.objects.get(id=userId)
    profil.friends.add(friend)
    return redirect('profil',userId)


def commentary(request, postId, userId):
    if request.method == 'POST':

        Commentaryform = CommentaryForm(request.POST)
        if Commentaryform.is_valid():
            text = Commentaryform.cleaned_data.get('text')
            author = request.user
            post = Post.objects.get(id=postId)
            commentary = Commentary.objects.create(text=text, author=author, post=post)
            commentary.save()

    return redirect('profil',userId)


def post(request, userId):

    Postform = PostForm(request.POST)
    if Postform.is_valid():
        title = Postform.cleaned_data.get('title')
        text = Postform.cleaned_data.get('text')
        author = request.user
        post = Post.objects.create(title=title, text=text, author=author)
        post.save()

    return redirect('profil', userId)