from django.shortcuts import render
import json
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import random
import os

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

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

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
    }

    return render(request, 'fashion/weather.html', context)