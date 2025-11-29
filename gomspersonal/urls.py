from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.books_landing, name="books_landing"),
]