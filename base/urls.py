from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutPage,name="logout"),
    path("room/<str:pk>",views.room,name="room"),
    path("contact/",views.contactus,name="contact"),
    path("create-room/",views.createRoom,name="create-room"),
    path("delete-room/<str:pk>",views.deleteRoom,name="delete-room"),
    path("update-room/<str:pk>",views.updateRoom,name="update-room"),

    
]
