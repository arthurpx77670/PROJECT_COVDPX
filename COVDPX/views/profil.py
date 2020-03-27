from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from COVDPX.models.db.db_profil import Profil
from django.http import HttpResponse


# user = User.objects.create_user('526', 'mkff5l@crepfes-bretonnes.com', 'm0nsup3rm0td3p4ss3')
# user1 = User.objects.create_user('935', 'm1sskfl@crepes-bretonnes.com', 'm0nsup3rm0td3p4ss3')
# profil1 = Profil.objects.create(user=user)
# profil1.friends.add(user1)


def profil(request, userId):
    user = User.objects.get(id=userId)
    users = User.objects.all()
    profil = Profil.objects.get(user_id=userId)
    friends = profil.friends.all()
    return render(request, "profil/profil_index.html", {"user": user, "users": users, "friends": friends})


def invitation(request, userId):
    profil = Profil.objects.get(user_id=request.user.id)
    friend = User.objects.get(id=userId)
    profil.friends.add(friend)
    return redirect('profil',userId)