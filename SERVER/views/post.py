from django.shortcuts import render, redirect
from SERVER.models.db.stats import Page
from SERVER.models.db.profile import Profile
from SERVER.models.db.post import Post, Commentary, Like
from SERVER.models.db.mission import Mission
from SERVER.models.forms.post import PostForm, CommentaryForm


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
            author = Profile.objects.get(user=request.user)
            post = Post.objects.create(title=title, text=text, author_id=author.id, file=file, price=price, deadline=deadline,description=False)
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

            return redirect('profile', userId)
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


def comment(request, postId, userId):
    if request.method == 'POST':
        Commentaryform = CommentaryForm(request.POST)
        if Commentaryform.is_valid():
            post = Post.objects.get(id=postId)
            author = Profile.objects.get(user=request.user)

            text = Commentaryform.cleaned_data.get('text')
            price = Commentaryform.cleaned_data.get('price')
            commentary = Commentary.objects.create(text=text, author_id=author.id, post_id=postId, price=price)
            commentary.save()

    return redirect('profile',userId)


def accept(request, userId, postId, commentaryId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        commentary = Commentary.objects.get(id=commentaryId)

        mission = Mission.objects.create(proposition=post, accept=commentary,description=False)
        mission.save()

        post.description = True
        post.save()

        commentary.description = True
        commentary.save()

    return redirect('profile',userId)