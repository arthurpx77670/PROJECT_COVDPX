from django.shortcuts import render
from SERVER.models.db.post import Like
from SERVER.models.forms.post import CommentaryForm


def cancel(request, missionId):



    return render(request, "wall/index.html")