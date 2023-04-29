from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserForm

def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your serwornet account is created")
        return render(request, "registration/signup.html")
    return render(request, "registration/signup.html")
