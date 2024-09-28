from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    fullname = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.fullname


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
