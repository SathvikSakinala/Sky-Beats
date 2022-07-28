# Create your views here.
from asyncio import mixins
from distutils.sysconfig import customize_compiler
from multiprocessing.dummy import JoinableQueue
from re import I, template
from urllib import response
from urllib.robotparser import RequestRate
import django
import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from matplotlib.style import context
from .forms import CreateUserForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# imported our models
from django.core.paginator import Paginator
from .models import *

@login_required(login_url='login')
def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

@login_required(login_url='login')
def player(request):

    '''if request.method == 'POST':
        user = request.user
        customer = request.user.customer
        song = Song.objects.get(id = song.get_id)
        content= request.POST.get('content')
        comment,created = Comment.objects.get_or_create(user=user,customer=customer,song = song,comment = content)
        comment.save()'''

    '''ids = Song.objects.get(id=my_id)'''
    songs = Song.objects.all()
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj,"songs":songs}
    return render(request,"player.html",context)

@login_required(login_url='login')
def main(request):
    context={}
    return render(request,"main.html",context)


class Homeview(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

@login_required(login_url='login')
def home(request):
    user = request.user
    songs = Song.objects.all()
    context={'songs': songs}
    return render(request,"home.html",context)

@login_required(login_url='login')
def beat(request):
    if request.user.is_authenticated():
        user = request.user
        songs = Song.objects.all()
        context={'songs': songs}
    else:
        context = {}
    return render(request,"beat.html",context)

def login(request):
    context={}
    return render(request, "login.html",context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            us = form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            bio = 'Write your bio :)'
            dob = '2001-12-29'
            customer, created = Customer.objects.get_or_create(user = us,name = user, email = email,Bio=bio,dob=dob)
            infos, created = Info.objects.get_or_create(user = us,name = user)
            #favourite, created = Favourite.objects.get_or_create(customer = customer,user = us,name = user)
            messages.success(request,'Account is created for '+ user)
            return redirect('user_login')

    context={'form': form}
    return render(request, "register.html",context)

def info(request):
    info = Info.objects.all()
    context={'info':info}
    return render(request,"info.html",context)

def usrlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect!')

    context={}
    return render(request, "user_login.html",context)


def privacy(request):
    context={}
    return render(request, "privacy.html",context)


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        logged = True
        paginator= Paginator(Song.objects.all(),1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        songs = Song.objects.all()
        name = request.user.username
        email = request.user.email
        #fav = Favourite.objects.all()
        #favitem = FavouriteItems.objects.all()
        context={'songs': songs, "page_obj":page_obj,"email":email ,"logged":logged,"name":name}
    else:
        context={}
    return render(request, "dashboard.html",context)


@login_required(login_url='login')
def favourite(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    songs = Song.objects.all()
    #fav = FavouriteItems.objects.all()
    name = request.user.username
    email = request.user.email
    context={'songs': songs, "page_obj":page_obj,"email":email ,"name":name}
    return render(request, "fav.html",context)

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def edit(request):
    #customer = request.user.customer
    #form = CustomerForm(instance=customer)
    #context = {"form":form}
    context={}
    return render(request,"edit.html",context)

'''
def Update(request):
    data = json.loads(request.body)
    
    songId = data['songId']
    action = data['action']
    print('Action : ',action)
    print('Song ID :', songId)

    customer = request.user.customer
    name = request.user.username
    user = request.user
    song = Song.objects.get(id = songId)
    favourite, created = Favourite.objects.get_or_create(customer = customer,name = name,user = user)

    favouriteitem,created = FavouriteItems.objects.get_or_create(favourite = favourite,song = song, add = False)

    if action == 'add':
        favouriteitem.add = True
    elif action == 'remove':
        favouriteitem.add = False

    favouriteitem.save()
    favourite.save()

    if favouriteitem.add == False:
        favouriteitem.delete()

    return JsonResponse('Song was added!', safe=False)'''

def Update(request):

    data = json.loads(request.body)
    
    songId = data['songId']
    action = data['action']
    print('Action : ',action)
    print('Song ID :', songId)

    customer = request.user.customer
    name = request.user.username
    user = request.user
    song = Song.objects.get(id = songId)
    #favourite, created = Favourite.objects.get_or_create(customer = customer,name = name,user = user)

    #favouriteitem,created = FavouriteItems.objects.get_or_create(favourite = favourite,song = song, add = False,user = user)

    if action == 'add':
        #favouriteitem.add = True
        song.fav = True
    elif action == 'remove':
        #favouriteitem.add = False
        song.fav = False

    #favouriteitem.save()
    #favourite.save()
    song.save()

    return JsonResponse('Song was added!', safe=False)

@login_required(login_url='login')
def upload(request):
    context = {}
    return render(request,"upload.html",context)


def songSearchResult(request):
    '''if request.method == "POST":
            searched = request.POST['searched']
            products = Product.objects.get_or_create(name__contains=searched)
            
            context = {'searched': searched,'cartItems': cartItems,'products' :products,'items': items,'logged': logged,'name': name}
            return render(request, 'store/search_result.html', context)
      else:
            print('Please search something!')
            context = {'cartItems': cartItems,'logged': logged,'name': name}
            return render(request, 'store/search_result.html', context)'''
    context={}
    return render(request, 'song_search.html', context)


'''
def comment(request):
    data = json.loads(request.body)
    
    songId = data['songId']
    print('Song ID :', songId)

    if request.method == 'POST':
        if request.POST.get('comment'):
            user = request.user
            song = Song.objects.get(id = songId)
            post=Comment()
            comment,created = Comment.objects.get_or_create(user=user,song = song)
            post.user = user
            post.song = song
            post.comment= request.POST.get('comment')
            post.dateoc = datetime.datetime.now()
            post.save()
            comment.save()

    user = request.user
    customer = request.user.customer
    song = Song.objects.get(id = songId)
    comm= request.POST.get('comment')
    comment,created = Comment.objects.get_or_create(user=user,customer=customer,song = song,comment = comm)
    comment.save()

    return JsonResponse('Comment posted successfully!', safe=False)

'''
