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
from SERVER.views import index
from SERVER.views import authenticate, profile, wall, post, mission
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.home),

    #form_auth
    path('registrate/', authenticate.registrate, name='registrate'),
    path('login/', authenticate.login_, name='login'),
    path('login/forget', authenticate.forget, name='forget'),
    path('login/forget/reboot?<int:userId>', authenticate.reboot, name='reboot'),

    #authenticate
    path('login/profile?<int:userId>', profile.profile, name='profile'),
    path('login/profile/logout', authenticate.logout_, name='logout'),
    path('login/profile?<int:userId>/edit', authenticate.edit, name='edit'),

    #profile
    path('login/profile?<int:userId>/invitation', profile.invite, name='invitation'),
    path('login/profile?<int:userId>/chat', profile.chat, name='chat'),
    path('login/profile?<int:userId>/chats', profile.chats, name='chats'),

    path('login/profile?<int:userId>/autocomplete', profile.autocomplete, name='autocomplete'),
    path('login/profileSearch', profile.profileSearch, name='profileSearch'),
    #path('login/profile?<int:userId>/refresh_chat', profile.refresh_chat, name='refresh_chat'),

    #post
    path('login/profile?<int:userId>/post', post.post, name='post'),
    path('login/profile/comment/<int:userId>/<int:postId>', post.comment, name='comment'),
    path('login/profile/accept/<int:userId>/<int:postId>/<int:commentaryId>', post.accept, name='accept'),
    path('login/profile/like/<int:userId>/<int:postId>', post.like, name='like'),
    path('login/profile/edit/<int:userId>/<int:postId>', post.edit, name='edit'),
    path('login/profile/delete/<int:userId>/<int:postId>', post.delete, name='delete'),
    path('login/profile?<int:userId>/take/<int:postId>', post.take, name='take'),


    #wall
    path('login/wall', wall.wall, name='wall'),

    #mission
    # path('login/cancel?<int:missionId>', mission.cancel, name='cancel'),
    path('login/deposit?<int:missionId>', mission.deposit, name='deposit'),
    path('login/opinion?<int:resultId>', mission.opinion, name='opinion'),


]
