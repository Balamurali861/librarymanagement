from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib import auth



# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password =  request.POST['username']
        user = authenticate(request,username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
    return Response("Logged In")