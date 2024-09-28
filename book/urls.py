from django.urls import path

from .views import (GenreAPIView, DetailGenreAPIView, AuthorListCreateAPIView, 
                    AuthorRetrieveUpdateDestroyAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path('genres/', GenreAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', DetailGenreAPIView.as_view(), name='genre-detail'),

    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),

    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
