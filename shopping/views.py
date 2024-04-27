from django.shortcuts import render, redirect
from shopping.models import Item
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from shopping.forms import AddItem


# Create your views here.
@require_http_methods(["GET", "POST"])
@login_required
def listings(request):
    """
    Displays all items in the database in descending order of date posted.

    Args:
        request (HttpRequest): The request object used to generate this view.

    Returns:
        render: A render object that displays the listings.html template with all items in the database.
    """
    try: 
        item_display = Item.objects.all().order_by('-date_posted')
    except Item.ObjectDoesNotExist: 
        item_display = {"No postings right now. Why not add something of your own?"}

    print(item_display)
    #KEEP COMMENTS FEATURE

    context = {
        'item_display' : item_display
    }

    return render(request, 'shopping/listings.html', context)

@login_required
def add_item(request): #the action tag on the form leads here
    """
    Adds a new item to the Item database.
    
    Args:
        request (HttpRequest): The request object used to generate this view. This one includes the POST request from the form.

    Returns:
        redirect: Redirects the user back to the listings page after adding a new item.
    """
    item_form = AddItem(request.POST, request.FILES)
    if item_form.is_valid():
        new_item = item_form.save(commit=False)
        new_item.user = request.user
        new_item.save()
        return redirect('listings')
    return redirect('listings')