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

def get_client_ip(request):
    # Check for X-Forwarded-For header (common in proxy environments)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # The first IP in the list is usually the real client IP
        ip = x_forwarded_for.split(',')[0]
    else:
        # Fallback to REMOTE_ADDR if no X-Forwarded-For header
        ip = request.META.get('REMOTE_ADDR')
    return ip


def log_tab_visit(request):
    tab_name = request.GET.get('tab_name', 'Unknown')
    # Get the client IP using the helper function
    client_ip = get_client_ip(request)

    # Log the visit with the tab name and client IP
    logger.info(f"Tab '{tab_name}' visited by {client_ip}")

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

