from django.shortcuts import render
from .models import book,photo

# Create your views here.
def personal_landing(request):
    return render(request, "personal_landing.html")
def books_landing(request):
    books = book.objects.all().order_by("id")
    return render(request, "books_landing.html", {"books": books})
def photography_landing(request):
    # Query the photo model to get all photo objects
    photos = photo.objects.all()
    return render(request, "photography.html", {"photos": photos})
