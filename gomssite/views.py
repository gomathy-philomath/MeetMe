from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gomspersonal.models import book
from gomsprofessional.models import careerHighlight
import logging
logger = logging.getLogger('visit_logger')

def log_tab_visit(request):
    tab_name = request.GET.get('tab_name', 'Unknown')
    logger.info(f"Tab '{tab_name}' visited by {request.META.get('REMOTE_ADDR')}")
    return JsonResponse({'status': 'success'})

def home(request):
    bookRead = book.objects.all()
    careerHilight = careerHighlight.objects.all()
    context = {
        'bookRead': bookRead,
        'careerHilight': careerHilight,
    }
    #logger.info(f"Home page visited by {request.META.get('REMOTE_ADDR')}")
    return render(request, 'home.html', context)

