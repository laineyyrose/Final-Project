from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy

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

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'registration/profile.html', {})

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    