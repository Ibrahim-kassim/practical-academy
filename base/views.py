from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login ,logout 


# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"an error accuring during registration")
    context = {"form":form}
    return render(request,"base/login_register.html" , context)

def logout():
    logout()

def home(request):
    rooms = Room.objects.all()
    context = {"leen":rooms}
    return render(request,"base/home.html",context)

def room(request,pk):
    # r = None
    # for ro in rooms:
    #     if ro['id'] == int(pk):
    #         r = ro
    r = Room.objects.get(id=pk)
    context ={"room":r}        
    return render(request,"base/room.html",context)

def contactus(request):
    return render(request,"base/contactus.html")

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request,"base/room_form.html",context)

def updateRoom(request,pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance=room)
     if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
     context = {"form":form}
     return render(request,"base/room_form.html",context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")

    context={"room":room}
    return render(request,"base/delete_room.html",context)

