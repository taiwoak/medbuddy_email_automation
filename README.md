# Medbuddy Email Automation Backend

This is a lightweight Django backend service that exposes an API endpoint (`/api/send-mail`) to trigger automated referral emails via the n8n workflow engine.

---

## Features

- Accepts email referral data from frontend or API clients
- Forwards data to n8n webhook (automation engine)
- Supports staging and production environments
- Simple error handling and response forwarding

---

## Tech Stack

- Python 3.x
- Django 4.x+
- Requests (for HTTP calls)
- Environment-based configuration using `.env`

---

## Installation

1. **Clone the project**

```bash
git clone https://github.com/taiwoak/medbuddy_email_automation.git
cd medbuddy-email-backend
```

2. **Set up a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create .env file**

```bash
DJANGO_SECRET_KEY=your_secret_key
DJANGO_ENV=staging  # or production
HOST=localhost,127.0.0.1 # yourproject.onrender.com
FRONTEND_URL=yourfrontendurl
N8N_WEBHOOK_URL_STAGING=https://your-n8n-staging-url.com/webhook
N8N_WEBHOOK_URL_PRODUCTION=https://your-n8n-production-url.com/webhook
CDN_SERVICE=http://localhost:8000  # Used by test_trigger.py or frontend
WEBSITE_URL=yourwebsiteurl
```

## Running the Server

```bash
python manage.py runserver
```

Visit http://localhost:8000/api/send-mail (POST only).


## Testing

1. **With Test file on Python**

```bash
python test_trigger.py
```

This file mimics a frontend call by sending test data to your /send-mail endpoint.

2. **Postman**

```bash
curl --location 'https://medbuddy-email-automation.onrender.com/api/send-mail' \
--header 'Content-Type: application/json' \
--data-raw '{
    "to": "dannyjanx@gmail.com",
    "from": "Medbuddy <taiwoakerele98@gmail.com>",
    "context": {
        "user_first_name": "Taiwo",
        "referred_user_name": "Daniel",
        "course_name": "Software Development",
        "currency": "USD",
        "referral_value": "1000",
        "referral_tracking_page_url": "https://medbuddyacademy.com/app/tracking",
        "recipient": "dannyjanx@gmail.com"
    },
    "template": "medbuddy_referral_followup"
}'
```

## Author

Built by Taiwo Akerele

