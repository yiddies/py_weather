import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='MyApp')

def get_location(city):
    location = geolocator.geocode(city)
    if location is None:
        print("Location not found. Please try again.")
        return None
    return location

def get_current_weather(location):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lat": location.latitude, "lon": location.longitude, "units": "I"}
    headers = {
        "X-RapidAPI-Key": "a5c1e156fdmsh2f0660f6bc4fcafp1d4769jsn64dc23f94b6e",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data

def get_future_weather(location, days):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
    querystring = {"lat": location.latitude, "lon": location.longitude, "units": "I", "days": days}
    headers = {
        "X-RapidAPI-Key": "a5c1e156fdmsh2f0660f6bc4fcafp1d4769jsn64dc23f94b6e",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data

def print_current_weather(location, data):
    city_name = location.address
    current_temp = data["data"][0]["temp"]
    weather_description = data["data"][0]["weather"]["description"]

    print("City Name:", city_name)
    print("Current Temperature:", current_temp)
    print("Weather Condition:", weather_description)
    print()

def print_future_weather(location, data, days):
    city_name = location.address

    for day in data["data"][:days]:
        date = day["valid_date"]
        min_temp = day["min_temp"]
        max_temp = day["max_temp"]
        weather_description = day["weather"]["description"]

        print("City Name:", city_name)
        print("Date:", date)
        print("Min Temperature:", min_temp)
        print("Max Temperature:", max_temp)
        print("Weather Condition:", weather_description)
        print()
