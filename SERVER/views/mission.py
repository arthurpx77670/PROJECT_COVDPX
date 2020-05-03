from django.shortcuts import render, redirect
from SERVER.models.db.mission import Mission, Result
from SERVER.models.forms.post import OpinionForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import json
from django.db.models import Q

@csrf_protect
def deposit(request,userId):
    if request.method == 'POST':
        missionId = request.POST.get('missionId')
        mission = Mission.objects.get(id=missionId)
        winnerId = int(request.POST.get('winnerId'))

        if winnerId == mission.proposition.author.id:
            looserId = mission.accept.author.id
        else:
            looserId = mission.proposition.author.id

        Result.objects.create(mission_id=missionId, winner_id=winnerId, looser_id=looserId, playerConfirm_id=request.user.profile.id)

        mission.description = True
        mission.save()

        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_protect
def confirm(request,userId):
    if request.method == 'POST':
        missionId = request.POST.get('missionId')
        winnerId = request.POST.get('winnerId')

        username = User.objects.get(profile__id=winnerId).username
        mission = Mission.objects.get(id=missionId)
        price = str(mission.proposition.price + mission.accept.price)

        if winnerId == request.user.profile.id:
            result = "Vous déclarer que vous avez gagné " + price
        else:
            result = "Vous déclarer que " + username + " a gagné " + price

        return HttpResponse(
            json.dumps({'result': result}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_protect
def validate(request,userId):
    if request.method == 'POST':
        missionId = request.POST.get('missionId')
        mission = Mission.objects.get(id=missionId)
        price = str(mission.proposition.price + mission.accept.price)

        if mission.result.winner == request.user.profile:
            result = "Vous avez gagné " + price
        else:
            result = "Vous avez perdu " + price

        return HttpResponse(
            json.dumps({"result" : result}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_protect
def finish(request,userId):
    if request.method == 'POST':
        missionId = request.POST.get('missionId')
        mission = Mission.objects.get(id=missionId)
        result = mission.result

        #stat
        price = mission.proposition.price + mission.accept.price
        addXp = int(result.winner.xp + price)
        while addXp >= 100:
            result.winner.level += 1
            addXp = addXp - 100

        result.winner.xp = addXp
        result.winner.number += 1
        result.winner.win += 1
        result.winner.portfolio += price
        result.winner.fund = result.winner.portfolio
        result.winner.save()

        result.looser.number += 1
        result.looser.portfolio -= price
        result.looser.fund = result.looser.portfolio
        result.looser.save()

        result.description = True
        result.save()

        return HttpResponse(
            json.dumps({}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
