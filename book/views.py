from django.shortcuts import render

from rest_framework.generics import (ListAPIView, RetrieveAPIView, DestroyAPIView, 
                                     CreateAPIView, UpdateAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import *
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer

# Create your views here.


class GenreAPIView(ListAPIView, CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    

class DetailGenreAPIView(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer








    