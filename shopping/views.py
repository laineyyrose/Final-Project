from django.shortcuts import render

# Create your views here.

#@login_required
def listings(request):
    return render(request, 'shopping/listings.html')