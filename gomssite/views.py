from django.http import HttpResponse
from django.shortcuts import render
from gomspersonal.models import book
from gomsprofessional.models import careerHighlight

def home(request):
    bookRead = book.objects.all()
    careerHilight = careerHighlight.objects.all()
    context = {
        'bookRead': bookRead,
        'careerHilight': careerHilight,
    }
    return render(request, 'home.html', context)