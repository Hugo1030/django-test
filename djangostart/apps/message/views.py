from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    # message = None
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print(message.name)
    # user_message = UserMessage()
    # user_message.name = "booby"
    # user_message.message = "helloworld"
    # user_message.address = "上海"
    # user_message.object_id = "lalala1"
    # user_message.save()
    return render(request, 'message_form.html')
