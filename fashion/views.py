from django.shortcuts import render
import json

# Create your views here.

#@login_required
def weather(request):
    """Shows the weather for the current day and suggests an 
    appropriate outfit based on it. Should use either the 
    OpenWeather or OpenMeteo API.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    return render(request, 'weather')