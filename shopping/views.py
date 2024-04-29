from django.shortcuts import render, redirect, get_object_or_404
from shopping.models import Item, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponseForbidden
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
    except Item.ObjectDoesNotExist: #TODO - go back and make sure this is the right exception
        item_display = {"No postings right now. Why not add something of your own?"}

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
        #this could've not used a form, but it's good practice & should be used when intaking an image
        new_item = item_form.save(commit=False)
        new_item.user = request.user
        new_item.save()
        return redirect('listings')
    return redirect('listings')

@login_required
def delete_item(request, pk):
    """
    Deletes item from  Item database.
    
    Args:
        request (HttpRequest): The request object used to generate this view. This one includes the PK of the item being deleted.

    Returns:
        redirect: Redirects the user back to the listings page after deleting an item.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        item.delete()
        return redirect('listings')
    else:
        return HttpResponseForbidden()

@login_required
def item(request, pk):
    """
    Displays a single item from the listings database and comments associated with it.

    Args:
        request (HttpRequest): The request object used to generate this view.
        pk (int): The primary key of the item to be displayed.

    Returns:
        render: A render object that displays the itemview.html template with the item specified by the primary key.
    """
    item = Item.objects.get(pk=pk)
    comments = Comment.objects.filter(item=item).order_by('-date_posted')

    context = {
        'item' : item,
        'comments' : comments,
    }
    return render(request, 'shopping/item.html', context)