"""PROJECT_COVDPX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from COVDPX.views import index
from COVDPX.views import authenticate, profil
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.home),

    #form_auth
    path('registration/', authenticate.registration, name='registration'),
    path('login/', authenticate.login_, name='login'),
    path('login/forget', authenticate.forget, name='forget'),
    path('login/forget/reboot?<int:userId>', authenticate.reboot, name='reboot'),

    #auth_profil
    path('login/profil?<int:userId>', profil.profil, name='profil'),
    path('login/profil/logout', authenticate.logout_, name='logout'),
    path('login/profil?<int:userId>/edit', authenticate.edit, name='edit'),

    #profil_action
    path('login/profil?<int:userId>/invitation', profil.invitation, name='invitation'),

]
