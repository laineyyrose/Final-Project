from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login') 
    else:
        return render(request, 'users/home.html', {})
        # return render(request, 'registration/profile.html', {'user': user})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

