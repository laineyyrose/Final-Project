from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import openmeteo_requests #OPENMETEO API IMPORTS (all the way down to random) - DO NOT TOUCH!
import requests_cache
import pandas as pd
from retry_requests import retry
import random
from django.core.cache import cache

# Create your views here.

@login_required
def thrift_map(request):
    """
    Author: Lainey
    Description: Dsiplays the html template with the google maps iframe and cards describing each thrift store on the map.

    Args:
        request (HttpRequest): The request object used to generate this view. 

    Returns:
        return (render): A render object that displays the thrift_map.html template.
    """
    return render(request, 'fashion/thrift_map.html', {})




@login_required
def weather(request):
    """
    Author: Andy
    Shows the weather for the current day and suggests an 
    appropriate outfit based on it. 

    Returns weather using OpenMeteo API and based on the weather returns 
    three random images from a gallery based on the types of weather.

    Args:
        request (HttpRequest): The request object used to generate this view. 

    Returns:
        return (render): A render object that displays the weather.html template with the weather daily (24hr) 
        data and current (15min) data, and a list of urls for the images to display.
    """

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 27.3364,
        "longitude": -82.5306,
        "current": ["temperature_2m", "apparent_temperature", "rain"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "precipitation_probability_max"],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "America/New_York",
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params) #this calls the openmeteo weather api

    response = responses[0] #this is the response for the API call

    # Get the date and time of the weather update
    update_time = pd.to_datetime(response.Current().Time(), unit='s', utc=True)

    # Convert the UTC time to the local timezone
    local_update_time = update_time.tz_convert('America/New_York')

    # Format the local update time as a string to display
    update_time_str = local_update_time.strftime("Updated %B %d, %Y, %I:%M %p")


    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = round(current.Variables(0).Value())
    current_apparent_temperature = round(current.Variables(1).Value())
    current_rain = current.Variables(2).Value()
    
    #rain_status should be the display based on the weather
    
    image_display = []
    image_numbers = random.sample(range(20), 3) #apparently this is bad on memory for large numbers, but we'll only have 20 images in total, so.
    if current_rain == 0:
        rain_status = 'Clear Skies'
        image_display.extend([f"clear/clear{image_numbers[0]}.jpg", f"clear/clear{image_numbers[1]}.jpg", f"clear/clear{image_numbers[2]}.jpg"])
    elif current_rain > 0.5:
        rain_status = 'Raining'
        image_display.extend([f"rain/rain{image_numbers[0]}.jpg", f"rain/rain{image_numbers[1]}.jpg", f"rain/rain{image_numbers[2]}.jpg"])
    else:
        rain_status = 'Sprinkling'
        image_display.extend([f"sprinkle/sprinkle{image_numbers[0]}.jpg", f"sprinkle/sprinkle{image_numbers[1]}.jpg", f"sprinkle/sprinkle{image_numbers[2]}.jpg"])

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy() 
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_uv_index_max = daily.Variables(2).ValuesAsNumpy()
    daily_precipitation_probability_max = daily.Variables(3).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["temperature_2m_max"] = [round(value, 1) for value in daily_temperature_2m_max]
    daily_data["temperature_2m_min"] = [round(value, 1) for value in daily_temperature_2m_min]
    daily_data["uv_index_max"] = [round(value, 1) for value in daily_uv_index_max]
    daily_data["precipitation_probability_max"] = [round(value, 1) for value in daily_precipitation_probability_max]

    context = {
        'current_temp' : current_temperature_2m, # weather for the last 15 minutes
        'current_apparent' : current_apparent_temperature, # what it feels like for the past 15min
        'rain_status' : rain_status,
        'image_display' : image_display, #images for the carousel to display based on weather
        'daily_data': daily_data,  # weather for the day
        'update_time': update_time_str # last time the weather was updated
    }

    return render(request, 'fashion/weather.html', context)


# Defining colors to use for the color_picker view.
colors = [
    {'name': 'RED', 'image_path': 'images/colors/red.jpg', 'description': 'Crimson Charge'},
    {'name': 'BLUE', 'image_path': 'images/colors/blue.jpg', 'description': 'Azure Depths'},
    {'name': 'GREEN', 'image_path': 'images/colors/green.jpg', 'description': 'Emerald Meadow'},
    {'name': 'PINK', 'image_path': 'images/colors/pink.jpg', 'description': 'Blush Blossom'},
    {'name': 'PURPLE', 'image_path': 'images/colors/purple.jpg', 'description': 'Royal Lavender'},
    {'name': 'SILVER', 'image_path': 'images/colors/silver.jpg', 'description': 'Sterling Gleam'},
    {'name': 'ORANGE', 'image_path': 'images/colors/orange.jpg', 'description': 'Tangerine Zest'},
    {'name': 'YELLOW', 'image_path': 'images/colors/yellow.jpg', 'description': 'Sunbeam Yellow'},
    {'name': 'BLACK', 'image_path': 'images/colors/black.jpg', 'description': 'Midnight Black'},
    {'name': 'WHITE', 'image_path': 'images/colors/white.jpg', 'description': 'Polar White'},
    {'name': 'TURQUOISE', 'image_path': 'images/colors/turquoise.jpg', 'description': 'Lagoon Wave'},
    {'name': 'NAVY', 'image_path': 'images/colors/navy.jpg', 'description': 'Deep Navy'}
]

def color_picker(request):
    """
    Author: Lainey
    Description: Displays a color of the day page with a randomly chosen color from the colors list.

    Returns:
        render: A render object that displays the color_picker.html template with the randomly chosen color and today's date.
    """
    color = cache.get('daily_color')
    if not color:
        color = random.choice(colors)
        cache.set('daily_color', color, timeout=86400)  # Cache for 24 hours
    today_date = timezone.now().strftime('%m-%d-%Y')  # how the date will be displyed on the page
    return render(request, 'fashion/color_picker.html', {'color': color, 'today_date': today_date})