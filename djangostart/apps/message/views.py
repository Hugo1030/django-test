from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print(message.address)
    return render(request, 'message_form.html')
