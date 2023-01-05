import requests
import datetime
from config import weather_token, bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard as k
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def stand_command(message: types.Message):
    await message.reply("Hi, I am a weather-bot, text me any city or town and I will try to find the current weather")

@dp.message_handler()
async def get_weather(message: types.Message):
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
        # getting coordinates of the city/town
        cords = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={message.text}&limit=1&appid={weather_token}")
        geo = cords.json()

        name = geo[0]['name']
        lat = geo[0]['lat']  # latitude
        lon = geo[0]['lon']  # longtitude

        r = requests.get(
            f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=alerts,daily,minutely,hourly&units=metric&appid={weather_token}")
        data = r.json()
        # pprint(data)

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

        await message.reply(f"The weather in {name}:\n{text_emoji}\nTemperature = {temp}°\n"
              f"Feels like {feels}°\nHumidity = {humidity}%\n"
              f"Sunrise time = {sunrise}\nSunset time = {sunset}")

    except:
        await message.reply('\U00002620 Check if the city/town name wrote correctly \U00002620')








if __name__ == '__main__':
    executor.start_polling(dp)
