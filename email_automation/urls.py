from django.urls import path
from .views import trigger_mail_workflow

urlpatterns = [
    path('send-mail', trigger_mail_workflow),
]
