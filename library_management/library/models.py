from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = ['username']
    ROLE_CHOICE = ((1, 'LIBRARIAN'),
                   (2, 'MEMBER'))
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    role = models.PositiveIntegerField(choices=ROLE_CHOICE, default=2)
    borrwed_books = models.PositiveIntegerField(null= False, default=0)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def detail(self):
        return self.username,self.email,self.get_role_display(),self.borrwed_books


class Books(models.Model):
    BOOK_STATUS = ((0, 'BORROWED'),
                   (1, 'AVAILABLE'))
    book_name = models.CharField(max_length=255, null=False)
    book_author = models.CharField(max_length=50, null=False)
    book_description = models.CharField(max_length=255, null=False, default="N/A")
    book_status = models.PositiveIntegerField(choices=BOOK_STATUS,null=False, default=1)

    def __str__(self):
        return self.book_name

    def display(self):
        return self.book_name,self.book_author,self.book_description,self.get_book_status_display()
