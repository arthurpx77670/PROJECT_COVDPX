from django.http import HttpResponse
from COVDPX.models.forms import loginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from COVDPX.models.forms import RegistrationForm, EditForm, RebootPswForm, ForgetPswForm
from django.contrib.auth import logout
from django.contrib.auth.models import User


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
                return redirect('profil')
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = loginForm()
    return render(request, 'authenticate/login.html', {'form': form, 'error': error})


def forget_psw(request):
    error = False
    if request.method == "POST":
        form = ForgetPswForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            if email and User.objects.filter(email=email).count():
                user = User.objects.get(email=email)  # Nous vérifions si les données sont correctes
                if user and user.username == username:  # Si l'objet renvoyé n'est pas None
                    return redirect('reboot_psw',user.id)
                else:  # sinon une erreur sera affichée
                    error = True
            else:
                error = True
    else:
        form = ForgetPswForm()
    return render(request, 'authenticate/forget_psw.html', {'form': form, 'error': error})


def reboot_psw(request,userId):
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
    return render(request, 'authenticate/reboot_psw.html',  {'form':form})


def logout_(request):
    logout(request)
    return redirect('/')


def edit(request, userId):
    user = User.objects.get(id=userId)
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            if username and User.objects.filter(username=username).count() and username != user.username:
                form.add_error('username',"This username is already in use. Please supply a different username")
            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect('profil')
    else:
        form = EditForm(initial={'username': user.username , 'first_name': user.first_name, 'last_name': user.last_name})
    return render(request, 'authenticate/edit.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            if email and User.objects.filter(email=email).exclude(username=username).count():
                form.add_error('email',"This email address is already in use. Please supply a different email address")
            else:
                form.save()
                return redirect('../login')
    else:
        form = RegistrationForm()
    return render(request, 'authenticate/registration.html', {'form': form})



