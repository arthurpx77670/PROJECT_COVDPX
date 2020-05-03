from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from SERVER.models.db.profile import Profile
from SERVER.models.db.post import Post, Commentary, Like
from SERVER.models.db.mission import Mission


@csrf_protect
def comment(request, postId, userId):
    if request.method == 'POST':

        post = Post.objects.get(id=postId)
        author = Profile.objects.get(user=request.user)

        text = request.POST.get('text')
        price = float(request.POST.get('price'))
        cotation = round((post.price / price) + 1, 1)

        author.fund = author.portfolio - post.price
        author.save()

        commentary = Commentary.objects.create(text=text, author_id=author.id, post_id=postId, price=price,cotation=cotation)
        commentary.save()

        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


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



@csrf_protect
def negociate(request, userId, postId):
    if request.method == 'POST':
        post = Post.objects.get(id=postId)
        newPriceUser = float(request.POST.get('price'))
        newCotation = round((post.price/newPriceUser)+1,1)
        newCotationUser = round(newCotation / (newCotation - 1), 1)

        fund = request.user.profile.fund

        return HttpResponse(
            json.dumps({'newCotation': newCotation, 'newCotationUser': newCotationUser,'fund': fund}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )