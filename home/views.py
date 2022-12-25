from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Project
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def privacy(request):
    return render(request, 'privacy.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        telephone = request.POST.get("telephone")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        send_mail("Customer contact", str(msg) + "\n" + telephone, str(email), ['eritten2@gmail.com'], fail_silently=True )
        messages.success(request, 'Thank you for contacting us')
        return redirect('/')
    return render(request, 'contact.html')

