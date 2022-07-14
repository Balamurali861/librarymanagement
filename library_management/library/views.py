from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib import auth
from rest_framework.views import APIView
from .serializers import Userserializer
from rest_framework.response import Response
from .models import Books
from .models import User
from django.contrib.auth import logout

from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
# Create your views here.
class Signup(APIView):
    def post(self,request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class Addbook(APIView):
    def post(self,request):
        data = request.data
        book = Books.objects.filter(book_name=data['book_name'],book_author=data['author_name'])
        if book.count():
            response = "Book Already Available"
        else:
            Books.objects.create(book_name=data['book_name'], book_author=data['book_author']
                                 , book_description=data['book_description'])
            response = "Book Added successfully"
        return Response(response)

class Updatebook(APIView):
    def post(self,request):
        data = request.data
        book = Books.objects.filter(book_name=data['book_name'],book_author=data['author_name'])
        if book.count():
            book[0].update(book_name =data['book_name'], book_author=data['book_author']
                           , book_description=data['book_description'])
            response = "Book updated successfully"
        return Response(response)


class Removebook(APIView):
    def post(self,request):
        data = request.data
        book = Books.objects.filter(book_name=data['book_name'],book_author=data['author_name'])
        response = "No book detected, Please check the Book Name and the author name"
        if book.count():
                book[0].delete()
                response = "Book deleted successfully"
        return response(response)

class Adduser(APIView):
    def post(self,request):
        data = request.data
        user = User.objects.filter(email=data['email'])
        if user.count():
            response = "User Already has an account, Please login"
        else:
            User.objects.create(username=data['username'], password=data['password'],
                                           email=data['email'], role=data['role'])
            response = "User Added successfully"
        return Response(response)

class Removeuser(APIView):
    def post(self,request):
        data = request.data
        user = User.objects.filter(email=data['email'])
        if user.count():
            if user[0].role == 1:
                response = "Librarian Account Can Not be Deleted"
            else:
                user[0].delete()
                response = "User Account Deleted"
        else:
            response = "No user was found"
        return Response(response)

class Viewuser(APIView):
    def post(self,request):
        data = request.data
        user = User.objects.filter(email=data['email'])
        if user.count():
            response = user[0].detail()
        else:
            response = "No user was found"
        return Response(response)

class Viewbooks(APIView):
    def get(self):
        output = []
        response = "Sorry no available books"
        book = Books.objects.filter(book_status=1)
        if book.count():
            for i in book:
                output.append(i.display())
        if output:
            return Response(output)
        else:
            return Response(response)

class Borrowbook(APIView):
    def post(self,request):
        data = request.data
        response = "Sorry no book found"
        book = Books.objects.filter(book_status=1,book_name=data['book_name'],book_author=data['book_author'])
        user = User.objects.get(email=request.user.email)
        if book.count():
            book[0].book_status = 0
            user.objects.updata(borrowed_books=user.borrwed_books+1)
            response =  "Thank you !! Have a good read"
        return Response(response)

class Returnbook(APIView):
    def post(self,request):
        data = request.data
        user = User.objects.get(email=request.user.email)
        response = "Incorrect entry or Book was not borrowed"
        book = Books.objects.filter(book_name=data['book_name'],book_author=data['book_author'],book_status=0)
        if book.count():
            book[0].book_status = 1
            user.objects.updata(borrowed_books=user.borrwed_books-1)
            response =  "Thank you for returning"
        return Response(response)

class Deleteself(APIView):
    def post(self,request):
        user = request.user
        find_user = User.objects.get(email=user.email)
        if find_user.email:
            if find_user.borrowed_book==0:
                request.user.delete()
                logout(request)
                return Response("Deleted, Logged out")
            else:
                return Response("Please return all the books before deleting account")
        else:
            return Response("Activity Failed")