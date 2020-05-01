from django.shortcuts import render, redirect
from SERVER.models.db.profile import Profile
from SERVER.models.db.post import Post, Commentary, Like
from SERVER.models.forms.post import PostForm, CommentaryForm
from django.views.decorators.csrf import csrf_protect
from SERVER.models.db.mission import Mission
from django.contrib.auth.models import User
from django.http import HttpResponse
import json


def post(request, userId):
    if request.method == 'POST':
        Postform = PostForm(request.POST, request.FILES)
        if Postform.is_valid():
            title = Postform.cleaned_data.get('title')
            text = Postform.cleaned_data.get('text')
            price = round(Postform.cleaned_data.get('price'),2)
            deadline = Postform.cleaned_data.get('deadline')
            cotation = round(Postform.cleaned_data.get('cotation'),1)
            if Postform.cleaned_data.get('file') is None:
                file = False
            else:
                file = Postform.cleaned_data.get('file')
            author = Profile.objects.get(user=request.user)
            priceUser = round(price * (cotation - 1),2)
            cotationUser = round(cotation/(cotation-1),1)

            post = Post.objects.create(title=title,
                                       text=text,
                                       author_id=author.id,
                                       file=file,
                                       price=price,
                                       deadline=deadline,
                                       description=False,
                                       cotation=cotation,
                                       cotationUser=cotationUser,
                                       priceUser=priceUser)
            post.save()
    return redirect('profile', userId)


def edit(request, userId, postId):
    post = Post.objects.get(id=postId)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            price = form.cleaned_data["price"]
            deadline = form.cleaned_data["deadline"]
            cotation = form.cleaned_data["cotation"]
            if form.cleaned_data.get('file') is None:
                file = False
            else:
                file = form.cleaned_data.get('file')

            post.title = title
            post.text = text
            post.file = file
            post.price = price
            post.file = file
            post.cotation = cotation
            post.deadline = deadline
            post.save()

            return redirect('profile', userId)
    else:
        if(post.file != 'False'):
            form = PostForm(initial={'title': post.title,
                                     'text': post.text,
                                     'file': post.file,
                                     'price': post.price,
                                     'deadline': post.deadline,
                                     'cotation' : post.cotation})
        else:
            form = PostForm(initial={'title': post.title,
                                     'text': post.text,
                                     'price': post.price,
                                     'deadline': post.deadline,
                                     'cotation' : post.cotation})

    return render(request, 'post/action/edit.html', {'form': form})


def delete(request, userId, postId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        post.delete()
    return redirect('profile',userId)


def like(request, postId, userId):
    if request.method == 'POST':
        author = Profile.objects.get(user_id=request.user.id)
        like = Like.objects.create(author_id=author.id, post_id=postId)
        like.save()
    return redirect('profile',userId)


@csrf_protect
def take(request, userId, postId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        author = request.user.profile
        commentary = Commentary.objects.create(description=True, price=post.priceUser, post=post, author = author, cotation=post.cotationUser)

        mission = Mission.objects.create(proposition=post, accept=commentary,description=False)
        mission.save()

        post.description = True
        post.save()
        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

