import requests
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='MyApp')
location = geolocator.geocode(input("Input City "))

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely"

querystring = {"lat": location.latitude, "lon": location.longitude}

headers = {
    "X-RapidAPI-Key": "a5c1e156fdmsh2f0660f6bc4fcafp1d4769jsn64dc23f94b6e",
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

print("City Name:", data["city_name"])