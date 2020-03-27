from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from COVDPX.models.db.db_profil import Profil, Post
from COVDPX.models.forms.form_profil import PostForm
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

    # post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            author = request.user
            post = Post.objects.create(tile=title, text=text, author=author)
            post.save()
    else:
        form = PostForm()

    return render(request, "profil/profil_index.html", {"user": user, "users": users, "friends": friends, "form": form, "posts": posts})


def invitation(request, userId):

    profil = Profil.objects.get(user_id=request.user.id)
    friend = User.objects.get(id=userId)
    profil.friends.add(friend)
    return redirect('profil',userId)