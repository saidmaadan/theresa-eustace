from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    return render(request, 'pages/home.html')

def about(request):
    
    return render(request, 'pages/about.html')


def disclaimer(request):
    
    return render(request, 'pages/disclaimer.html')

def privacy(request):
    
    return render(request, 'pages/privacy.html')

def terms(request):
    
    return render(request, 'pages/terms.html')

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        to_email = 'mm@theresaeustace.com'
        
        send_email = EmailMessage(subject, message_body, email, to=[to_email])
        send_email.send()
        
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')

def thankyou(request):
    
    return render(request, 'pages/thankyou.html')

def already_subscribed(request):
    
    return render(request, 'pages/already-subscribed.html')



# Create your views here.
