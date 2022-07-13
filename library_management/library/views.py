from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib import auth
from rest_framework.views import APIView
from .serializers import Userserializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
# Create your views here.
class Signup(APIView):
    def post(self,request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):
    def post(self,request):
        user_name = request.data['user_name']
        password = request.data['password']

        user = User.objects.filter(user_name = user_name).first()
        if user is None:
            raise AuthenticationFailed('Sorry, User not registered')

        if not user.check_password(password):
            raise AuthenticationFailed('Sorry, The password is incorrect')
        expiry = str(datetime.datetime.now()+datetime.timedelta(minutes=60))
        born = str(datetime.datetime.now())
        payload = {
            'id': user.id,
            'expiry': expiry,
            'born': born,
        }
        print(payload)
        json_token = jwt.encode(payload,'secret',algorithm='HS256')
        print(json_token)
        return Response({'jwt':json_token})
