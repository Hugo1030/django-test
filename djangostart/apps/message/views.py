from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def getform(request):
    all_messages = UserMessage.objects.filter(name='hugo', address='beijing')
    for message in all_messages:
        message.delete()
    # user_message = UserMessage(name='hugo2', email='2@2.com', address='beijing2', message='HelloWorld2', object_id='HelloWorld2')
    # user_message.save()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        user_message = UserMessage(name=name, email=email, address=address, message=message, object_id='HelloWorld3')
        user_message.save()

    return render(request, 'message_form.html')
