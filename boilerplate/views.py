from .tasks import send_msg_task
from django.http import HttpResponse
import json

def send_msg_view(request):
    message = "Hello World"
    send_msg_task.delay(message)
    return HttpResponse(json.dumps({"success": True, "message": message}))