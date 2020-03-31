from SERVER.models.forms.forms_auth import loginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from SERVER.models.forms.forms_auth import RegistrationForm, EditForm, RebootPswForm, ForgetPswForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from SERVER.models.db.db_profil import Profil


def login_(request):
    error = False
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('profil', user.id)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = loginForm()
    return render(request, 'authenticate/auth_login.html', {'form': form, 'error': error})


def forget(request):
    error = False
    if request.method == "POST":
        form = ForgetPswForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            if email and User.objects.filter(email=email).count():
                user = User.objects.get(email=email)  # Nous vérifions si les données sont correctes
                if user and user.username == username:  # Si l'objet renvoyé n'est pas None
                    return redirect('reboot',user.id)
                else:  # sinon une erreur sera affichée
                    error = True
            else:
                error = True
    else:
        form = ForgetPswForm()
    return render(request, 'authenticate/auth_forget.html', {'form': form, 'error': error})


def reboot(request,userId):
    user = User.objects.get(id=userId)
    if request.method == "POST":
        form = RebootPswForm(request.POST)
        if form.is_valid():
            psw = password = form.cleaned_data.get('password1')
            user.set_password(psw)
            user.save()
            return redirect('login')
    else:
        form = RebootPswForm()
    return render(request, 'authenticate/auth_reboot.html', {'form':form})


def logout_(request):
    logout(request)
    return redirect('/')
from django.http import HttpResponse


def edit(request, userId):
    user = User.objects.get(id=userId)
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            picture = form.cleaned_data["picture"]
            if username and User.objects.filter(username=username).count() and username != user.username:
                form.add_error('username',"This username is already in use. Please supply a different username")
            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                if picture:
                    profil = Profil.objects.get(user_id=userId)
                    profil.picture = picture
                    profil.save()
                return redirect('profil', user.id)
    else:
        form = EditForm(initial={'username': user.username , 'first_name': user.first_name, 'last_name': user.last_name})
    return render(request, 'authenticate/auth_edit.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if email and User.objects.filter(email=email).exclude(username=username).count():
                form.add_error('email',"This email address is already in use. Please supply a different email address")
            else:
                form.save()
                user = User.objects.get(username=username)
                Profil.objects.create(user=user)
                return redirect('../login')
    else:
        form = RegistrationForm()
    return render(request, 'authenticate/auth_regist.html', {'form': form})



