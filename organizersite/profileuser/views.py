from pyexpat.errors import messages
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register_view(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('main') 
    else: 
        form = CustomUserCreationForm() 
    return render(request, 'registration.html', {'form': form}) 

def login_view(request): 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user) 
            return redirect('main') 
        else: 
            messages.error(request, 'Invalid username or password') 
    return render(request, 'login.html', {})
 
def logout_view(request): 
    logout(request) 
    return redirect('home')

@login_required(login_url='login')
def main(request):
    return render(request, 'main.html')
