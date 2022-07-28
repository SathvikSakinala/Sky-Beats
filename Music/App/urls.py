from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.login, name="login"),
    path("info/",views.info, name="info"),
    path("home/", views.home, name="home"),
    path("beat/", views.beat, name="beat"),
    path("main/", views.main, name="main"),
    path("fav/", views.favourite, name="fav"),
    path("update/", views.Update, name="update"),
    path("logout/", views.logout, name="logout"),
    path("player/", views.player, name="player"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user_login/", views.usrlogin, name="user_login"),
    path("edit_profile/", views.edit, name="edit_profile"),
    path("upload_songs/", views.upload, name="upload_songs"), 
    path("privacy_policy/", views.privacy, name="privacy_policy"),
    path('song_search/', views.songSearchResult, name="song_search"),
]