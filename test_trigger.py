
# Set up Django environment manually
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medbuddy_email_automation.settings")
django.setup()


from postmark_client import post_to_cdn_postmark_service

payload = {
    "to": "dannyjanx@gmail.com",
    "from": "Medbuddy <info@medbuddyafrica.com>",
    "context": {
        "user_first_name": "Daniel",
        "referred_user_name": "Akinniyi",
        "course_name": "Software Development",
        "currency": "USD",
        "referral_value": "1000",
        "referral_tracking_page_url": "https://medbuddyacademy.com/app/tracking",
        "recipient": "dannyjanx@gmail.com"
    },
    "template": "medbuddy_referral_followup"
}

response = post_to_cdn_postmark_service("/send-mail", payload)
print(response)



# print("Status Code:", response.status_code)
# print("Response:", response.json())
