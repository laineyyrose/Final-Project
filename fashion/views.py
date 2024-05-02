from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import openmeteo_requests #OPENMETEO API IMPORTS (all the way down to random) - DO NOT TOUCH!
import requests_cache
import pandas as pd
from retry_requests import retry
import random

# Create your views here.

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