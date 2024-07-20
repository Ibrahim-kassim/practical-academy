from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

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
