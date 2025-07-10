import requests
from django.conf import settings

def post_to_cdn_postmark_service(path, payload):
    """Sends the payload to a Django internal API endpoint."""
    try:
        url = f"{settings.CDN_SERVICE.rstrip('/')}/api{path}"
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}
