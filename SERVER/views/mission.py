from django.shortcuts import render, redirect
from SERVER.models.db.mission import Mission, Result
from SERVER.models.forms.post import DepositForm, OpinionForm


# def cancel(request, missionId):
#     mission = Mission.objects.get(id=missionId)
#     mission.delete()
#
#     return redirect ("profile/index.html", request.user.id)


def deposit(request, missionId):

    if request.method == 'POST':
        form = DepositForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            result = Result.objects.create(file=file, mission_id=missionId)
            mission = Mission.objects.get(id=missionId)
            mission.description = True
            mission.save()
            return redirect("profile", request.user.id)
    else:
        form = DepositForm()
    return render(request, 'mission/action/deposit.html', {'form': form})


def opinion(request, resultId):

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.cleaned_data.get('opinion')
            mark = form.cleaned_data.get('mark')

            result = Result.objects.get(id=resultId)
            result.opinion = opinion
            result.mark = mark
            result.save()

            return redirect("profile", request.user.id)
    else:
        form = OpinionForm()
    return render(request, 'mission/action/opinion.html', {'form': form})





