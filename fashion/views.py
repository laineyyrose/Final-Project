from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def thrift_map(request):
    return render(request, 'thrift_map.html', {})
