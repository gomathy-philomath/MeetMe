from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gomspersonal.models import book
from gomsprofessional.models import careerHighlight
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import logging, os
logger = logging.getLogger('visit_logger')

@csrf_exempt
def get_logs(request):
    try:
        log_file_path = os.path.join(settings.BASE_DIR, 'logs', 'website.log')

        # Check if the log file exists
        if not os.path.exists(log_file_path):
            return JsonResponse({'error': 'Log file not found'}, status=404)

        # Read the log file content
        with open(log_file_path, 'r') as file:
            logs = file.readlines()

        # Return the logs as a JSON response
        return JsonResponse({'logs': logs}, status=200)

    except Exception as e:
        logger.error(f"Error reading log file: {e}")
        return JsonResponse({'error': str(e)}, status=500)

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

