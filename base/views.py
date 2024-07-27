from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.


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