from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from django.views.generic import DetailView, CreateView
from shopping.models import Profile
from django.shortcuts import get_object_or_404
from shopping.models import Item


def logout_view(request):
    logout(request)
    return redirect("login")

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self):
        return self.request.user
    
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_items = Item.objects.all().filter(user=user.pk).order_by('-date_posted') #shows user's specific items
        context["pageuser"] = user
        context['items'] = user_items
        return context
    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['first_name', 'last_name', 'bio', 'profile_pic', 'pinterest_url', 'venmo_url']
    success_url = reverse_lazy('home_page')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    success_url = reverse_lazy('home_page')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def logout_and_redirect(request):
    logout(request)
    return redirect('login')  
