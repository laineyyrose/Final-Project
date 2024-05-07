from django.shortcuts import render, redirect, get_object_or_404
from shopping.models import Item, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponseForbidden
from shopping.forms import AddItem, EditItem, AddComment
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
@require_http_methods(["GET", "POST"])
@login_required
def listings(request):
    """
    Author: Andy
    Displays all items in the database in descending order of date posted.

    Args:
        request (HttpRequest): The request object used to generate this view.

    Returns:
        render: A render object that displays the listings.html template with all items in the database.
    """
    if request.method == 'GET':
        
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')

        item_display = Item.objects.all().order_by('-date_posted')

        # Filter by minimum price if provided
        if min_price != '':
            item_display = item_display.filter(price__gte=min_price)

        # Filter by maximum price if provided
        if max_price != '':
            item_display = item_display.filter(price__lte=max_price)

        if Item.objects.all().exists() == False:
            item_display = {}

    context = {
        'item_display' : item_display
    }

    return render(request, 'shopping/listings.html', context)

@login_required
def add_item(request): #the action tag on the form leads here
    """
    Author: Andy
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

#Andy
@login_required
def delete_item(request, pk):
    """
    Author: Andy
    Deletes item from  Item database.
    
    Args:
        request (HttpRequest): The request object used to generate this view. This one includes the PK of the item being deleted.

    Returns:
        redirect: Redirects the user back to the listings page after deleting an item.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.user: #check if the user is the owner of the item
        return HttpResponseForbidden()
    if request.method == 'POST': 
        item.delete()
        return redirect('listings')
    else:
        return HttpResponseForbidden()
    
@login_required
def edit_item(request, pk):
    """
    Author: Andy
    Edits an item in the Item database.

    Args:
        request (HttpRequest): The request object used to generate this view. This one includes the POST request from the edit form.
        pk: The primary key of the item to be edited.

    Returns:
        redirect: Redirects the user back to the item page after editing the item.
    """
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = EditItem(request.POST, request.FILES, instance=item)
        if form.is_valid(): #simple validation
            form.save()
            return redirect('item', pk=pk)
    else:
        form = EditItem(instance=item)
    return redirect('item', pk=pk)

@login_required
def item(request, pk):
    """ 
    Author: Andy
    Displays a single item from the listings database and comments associated with it.

    Args:
        request (HttpRequest): The request object used to generate this view.
        pk: The primary key of the item to be displayed.

    Returns:
        render: A render object that displays the itemview.html template with the item specified by the primary key.
    """
    item = get_object_or_404(Item, pk=pk)
    try:
        comments = Comment.objects.filter(item=item).order_by('-date_posted')
    except Comment.objects.filter(item=item).exists() == False:
        comments = {None}
    editform = EditItem(instance=item)

    context = {
        'item' : item,
        'comments' : comments,
        'editform' : editform, #for modal consistency sake
    }
    return render(request, 'shopping/item.html', context)

@login_required
def add_comment(request, pk):
    """
    Author: Andy
    Adds a comment to an item in the database.

    Args:
        request (HttpRequest): The request object used to generate this view.
        pk (int): The primary key of the item to be commented on and redirected to after posting.

    Returns:
        render: A render object that displays the item.html template with the item specified by the primary key, with added comment.
    """
    item = Item.objects.get(pk=pk)
    comment_form = AddComment(request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.item = item
        new_comment.save()
        return redirect('item', pk=pk)
    return redirect('item', pk=pk)

@login_required
def delete_comment(request, pk):
    """Removes the text of the comment and replaces it with a message saying it has been deleted.

    Args:
        request (HttpRequest): The request object used to generate this view. Specifically, this is probably post.
        pk : The unique primary key of the comment.

    Returns:
        redirect: Redirects the user back to the item page after deleting a comment.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        comment.delete_text()
        return redirect('item', pk=comment.item.pk)
    else:
        return HttpResponseForbidden()
    

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ['title', 'author', 'body']