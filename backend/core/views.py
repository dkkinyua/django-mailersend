from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.urls import reverse
from .forms import LoginForm, SignupForm
from .utils import send_email 

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .forms import LoginForm, SignupForm

def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("core:login"))
    else:
        form = SignupForm()
    return render(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("core:home"))
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {"form": form})

def home(request):
    message = "Hello world, you are home."

    return render(request, 'core/index.html', {"message": message})


def send_email_user(request):
    user = request.user
    email = user.email
    error_message = "Email not sent"

    if not email:
        return HttpResponse(error_message)
    
    try:
        send_email(email) 
        return render(request, 'core/send_email.html', {"message": "Email sent"})
    except Exception as e:
        return HttpResponse(f"{error_message}: {str(e)}")
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:login'))