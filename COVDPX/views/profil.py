from COVDPX.models.user import Profil
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# user = User.objects.create_user('hj', 'mkl@crepes-bretonnes.com', 'm0nsup3rm0td3p4ss3')
# profil1 = Profil.objects.create(user=user)


def profil(request,userId):
    user = User.objects.get(id=userId)
    users = User.objects.all()
    return render(request, "profil/profil_index.html", {"user":user,"users": users})