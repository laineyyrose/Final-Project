from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
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
    """
    Author: Lainey
    Logout view function that logs out the user and redirects to the login page.

    Args:
        request (HttpRequest): The request object for the current view.

    Returns:
        redirect: Redirects to the login page.
    """
    logout(request)
    return redirect("login")

class UserRegisterView(generic.CreateView):
    """
    Author: Lainey
    View for user registration.

    This view handles the registration of new users by using the SignUpForm.
    After successful registration, the user is redirected to the login page.

    Attributes:
        form_class (class): The form class to use for user registration.
        template_name (str): The name of the template to render for user registration.
        success_url (str): The URL to redirect to after successful registration.
    """

    form_class = SignUpForm  # Use SignUpForm for user registration
    template_name = 'registration/register.html'  # Render the register.html template
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration


class UserEditView(generic.UpdateView):
    """
    Author: Lainey
    A view for editing user profiles.

    This view allows users to edit their profile information.

    Attributes:
        form_class (class): The form class used for editing the profile.
        template_name (str): The name of the template used for rendering the edit profile page.
        success_url (str): The URL to redirect to after successfully editing the profile.

    Methods:
        get_object: Retrieves the user object to be edited.

    """

    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self):
        """
        Retrieves the user object to be edited.

        Returns:
            User: The user object to be edited.

        """
        return self.request.user


    
class ShowProfilePageView(DetailView): #LAINEY MADE THIS ONE
    """
    Author: Lainey
    View for displaying a user's profile page.

    Attributes:
        model (Profile): The model used for retrieving the user's profile.
        template_name (str): The name of the template used for rendering the profile page.
    """
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
    """
    Author: Lainey
    A view for editing a user's profile page.
    """
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['first_name', 'last_name', 'bio', 'profile_pic', 'pinterest_url', 'venmo_url']

    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.
        """
        # Assuming your Profile model has a `pk` to use for the URL
        return reverse('show_profile_page', kwargs={'pk': self.object.pk})
    

class CreateProfilePageView(CreateView):
    """
    Author: Lainey
    View for creating a user profile page.
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    
    def form_valid(self, form):
        """
        Called when form data is valid.
        Sets the user attribute of the form instance to the current user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.
        Assumes the Profile model has a `pk` field to use for the URL.
        """
        return reverse('show_profile_page', kwargs={'pk': self.object.pk})
    
def logout_and_redirect(request):
    """
    Author: Lainey
    Logs out the user and redirects them to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the login page.
    """
    # Logout the user
    logout(request)

    # Redirect to the login page
    return redirect('login')
