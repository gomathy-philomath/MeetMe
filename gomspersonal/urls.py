from django.urls import path
from . import views

app_name = "gomspersonal"

urlpatterns = [
    path("about/", views.personal_landing, name="personal_landing"),
    path("books/", views.books_landing, name="books_landing"),
    path("photography/", views.photography_landing, name="photography_landing"),
]