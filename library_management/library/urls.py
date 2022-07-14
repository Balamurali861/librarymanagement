"""library_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from .views import *
urlpatterns = [
    path('register',Signup.as_view()),
    path('addbook',Addbook.as_view()),
    path('updatebook',Updatebook.as_view()),
    path('removebook',Removebook.as_view()),
    path('adduser',Adduser.as_view()),
    path('removeuser',Removeuser.as_view()),
    path('viewuser',Viewuser.as_view()),
    path('viewbooks',Viewbooks.as_view()),
    path('borrowbook',Borrowbook.as_view()),
    path('deleteuser',Deleteself.as_view()),
    path('returnbook',Returnbook.as_view()),
]
