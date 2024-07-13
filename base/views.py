from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Python Basics', 'description': 'Learn the fundamentals of Python programming'},
    {'id': 2, 'name': 'Django Framework', 'description': 'Explore web development with Django'},
    {'id': 3, 'name': 'Data Science', 'description': 'Dive into data analysis and machine learning'},
    {'id': 4, 'name': 'Web Design', 'description': 'Master HTML, CSS, and responsive design'},
]


def home(request):
    context = {"leen":rooms}
    return render(request,"base/home.html",context)

def room(request,pk):
    r = None
    for ro in rooms:
        if ro['id'] == int(pk):
            r = ro
    context ={"room":r}        
    return render(request,"base/room.html",context)

def contactus(request):
    return render(request,"base/contactus.html")
