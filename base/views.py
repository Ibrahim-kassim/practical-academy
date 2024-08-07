from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room , Topic
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            auth_login(request,user)
            return redirect("home")
        else:
            messages.error(request,"an error accuring during registration")
    context = {"form":form}
    return render(request,"base/login_register.html" , context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('login')  # Return here to avoid further execution

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
    context = {"page": page}
    return render(request, "base/login_register.html", context)

def logoutPage(request):
    logout(request)
    return redirect("home")

def home(request):
    q= request.GET.get("q") if request.GET.get("q") != None else ''
    topics = Topic.objects.all()
    rooms = Room.objects.filter(Q(topic__name__icontains =q) |
                                Q(name__icontains= q) |
                                Q(host__username__icontains =q))
    roomNumber=rooms.count()

    context = {"leen":rooms , "topics":topics,"roomNumber":roomNumber}
    return render(request,"base/home.html",context)

def room(request,pk):
    # r = None
    # for ro in rooms:
    #     if ro['id'] == int(pk):
    #         r = ro
    r = Room.objects.get(id=pk)
    context ={"room":r,}        
    return render(request,"base/room.html",context)

def contactus(request):
    return render(request,"base/contactus.html")

@login_required(login_url="/login")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request,"base/room_form.html",context)

@login_required(login_url="/login")
def updateRoom(request,pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance=room)
     if request.user != room.host:
        return HttpResponse("you are not allowed here")
     if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
     context = {"form":form}
     return render(request,"base/room_form.html",context)


@login_required(login_url="/login")
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("you are not allowed here")
    if request.method == "POST":
        room.delete()
        return redirect("home")

    context={"room":room}
    return render(request,"base/delete_room.html",context)

