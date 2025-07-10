import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def trigger_mail_workflow(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests allowed'}, status=405)

    try:
        payload = json.loads(request.body)

        required_keys = ['to', 'from', 'context', 'template']
        for key in required_keys:
            if key not in payload:
                return JsonResponse({'error': f'Missing key: {key}'}, status=400)

        response = requests.post(settings.N8N_WEBHOOK_URL, json=payload)
        response.raise_for_status()

        return JsonResponse({'status': 'Workflow triggered successfully, Email Sent!'})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
