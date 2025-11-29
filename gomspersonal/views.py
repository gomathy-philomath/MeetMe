from django.shortcuts import render
from .models import book

# Create your views here.
def books_landing(request):
    books = book.objects.all().order_by("id")
    return render(request, "books_landing.html", {"books": books})
