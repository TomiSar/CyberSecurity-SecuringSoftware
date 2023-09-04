from django.http import HttpResponse
from .models import Message
import random


def homePageView(request):
    try:
        messageID = int(request.GET["id"])
        responseMessage = Message.objects.get(pk=messageID).content
    except:
        responseMessage = "Message ID not found!"

    return HttpResponse(responseMessage)
