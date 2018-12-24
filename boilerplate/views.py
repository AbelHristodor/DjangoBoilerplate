from django.http import HttpResponse
from django.shortcuts import render

from .tasks import send_msg_task

import json

def send_msg_view(request):
    message = "Hello World"
    send_msg_task.delay(message)
    return HttpResponse(json.dumps({"success": True, "message": message}))

def home_view(request):
    return render(request, "pages/homepage.html")