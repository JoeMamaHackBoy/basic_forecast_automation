import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
GEOLOCATION_URL = "http://api.openweathermap.org/geo/1.0/direct?"
def run_forecast():
    city = input("Choose the city for weather forcast: ")
    request_url_geolocation = f"{GEOLOCATION_URL}q={city}&appid={API_KEY}"
    response_geolocation = requests.get(request_url_geolocation)
    geolocation_data = response_geolocation.json()
    print(geolocation_data)
    lat = geolocation_data[0]["lat"]
    lon = geolocation_data[0]["lon"]
    print(f"latitude = {lat} longtitude = {lon}")
    request_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        current_weather = data["weather"][0]["description"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        temperature = data["main"]["temp"] - 273.15
        temperature = round(temperature, 0)
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"] 
        print(f"Chosen City: {city_name}")
        print(f"Weather: {current_weather}")
        print(f"Temperature: {temperature}")
        print(f"Atmospheric Pressure: {pressure}hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed}m/s")
        print(f"Wind Direction: {wind_direction} Degrees Bearing")
        
    else:
        print("Response error value not found, sorry for any inconvenience")
run_forecast()
