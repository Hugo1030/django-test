from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name='jane')
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html', {
        "my_message":message
    })
