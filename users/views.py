from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from django.views.generic import DetailView, CreateView
from shopping.models import Profile
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseNotAllowed
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
    
class ShowProfilePageView(DetailView): #LAINEY MADE THIS ONE
    model = Profile
    template_name = 'registration/user_profile.html'

    def dispatch(self, request, *args, **kwargs):
        """Author: Andy
        Dispatch method for the ShowProfilePageView class. This method is called when the view is loaded.
        It overrides the dispatch method in the DetailView class to handle the case where the profile doesn't exist.

        Returns:
            self (ShowProfilePageView): The ShowProfilePageView object.
            request (HttpRequest): The request object for the current view that DetailView bases its render off of.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. In this case, it'll be the viewed user's primary key.

        Raises:
            Http404: Raises an exception if the profile doesn't exist to trigger the handle_profile_not_found method.
        
        Returns:
            super().dispatch: Returns the dispatch method from the parent class if the profile exists.
        """
        if request.method == 'GET':
            try:
                self.object = self.get_object()
            except Http404:
                # Profile doesn't exist, call a separate method for handling this case
                return self.handle_profile_not_found(request, *args, **kwargs)
            else:
                return super().dispatch(request, *args, **kwargs)
        else:
            # Handle other HTTP methods here if needed
            return HttpResponseNotAllowed(['GET'])

    def handle_profile_not_found(self, request, *args, **kwargs): #this is a custom method to handle the case where the profile doesn't exist so it doesn't 404
        """Author: Andy
        Handle the case where the profile doesn't exist. 
        This method will be called after a GET when the profile doesn't exist.

        Args:
            self (ShowProfilePageView): The ShowProfilePageView object.
            request (HttpRequest): The request object for the current view that DetailView bases its render off of.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. In this case, it'll be the viewed user's primary key.

        Returns:
            redirect: Redirects to the show profile page, and passes the pk back through.
        """
        # Get the user object
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        # Create a new profile associated with the user
        profile = Profile.objects.create(user=user)
        # Redirect to the profile page
        return redirect('show_profile_page', pk=profile.pk)

    def get_context_data(self, *args, **kwargs):
        """Author: Lainey (edited by Andy)
        Get the context data for the ShowProfilePageView class. This method is called when the view is loaded.

         Args:
            self (ShowProfilePageView): The ShowProfilePageView object. This just passes the context to it.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. In this case, it'll be the viewed user's primary key.

        Returns:
            context: The context data for the ShowProfilePageView class.
        """
        context = super().get_context_data(*args, **kwargs)
        user_items = Item.objects.filter(user=self.object.pk).order_by('-date_posted')
        context["pageuser"] = self.object
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
