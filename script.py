import requests
from pprint import pprint
from config import weather_token
import datetime
def get_weather(city, weather_token):
    emoji = {
        "Clear": "Clear sky \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }



    try:
        #getting coordinates of the city/town
        cords = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_token}")
        geo = cords.json()

        name = geo[0]['name']
        lat = geo[0]['lat'] #latitude
        lon = geo[0]['lon'] #longtitude

        r = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=alerts,daily,minutely,hourly&units=metric&appid={weather_token}")
        data = r.json()
        #pprint(data)

        weather_description = data['current']['weather'][0]['main']
        if weather_description in emoji:
            text_emoji = emoji[weather_description]
        else:
            text_emoji = "Check the window, I can't understand what is the weather"
        temp = data['current']['temp']
        feels = data['current']['feels_like']
        humidity = data['current']['humidity']
        sunrise = datetime.datetime.fromtimestamp(data['current']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['current']['sunset'])


        print(f"The weather in {name}:\n{text_emoji}\nTemperature = {temp}°\n"
              f"Feels like {feels}°\nHumidity = {humidity}%\n"
              f"Sunrise time = {sunrise}\nSunset time = {sunset}")

    except Exception as ex:
        print('ex')
        print('Check if the city/town name wrote correctly')
def main():
    city = input("Write the city/town name:")
    get_weather(city, weather_token)

if __name__ == '__main__':
    main()
