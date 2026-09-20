from pickletools import dis

import aiohttp

from aiogram import Bot, Dispatcher, dispatcher
from aiogram.filters import Command
from aiogram.types import Message


TOKEN = "8973344987:AAH5Dv3UhEsei0AgWORASyjDgfbxke1DALc"
WEATHER_API_KEY = "b56efe80b9a85be43256197078115e44"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("weather"))
async def command_weather(message: Message) -> None:

    url = "https://api.openweathermap.org/data/2.5/weather?q=Urgench,UZ&appid=b56efe80b9a85be43256197078115e44&units=metric&lang=ru"


    params = {
        "q": "Urganch,UZ",
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:

            if response.status != 200:
                await message.answer("eror")
                return

            data = await response.json()


    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    text = (
        "🌤 Погода в Ургенче\n\n"
        f"🌡 Температура: {temperature}°C\n"
        f"😊 ощущается как: {feels_like}\n"
        f"💧 влажност: {humidity}%\n"
        f"☁️ состояние: {description}"
    )

    await message.answer(text)

@dp.message(Command("usd"))
async def command_usd(message: Message) -> None:
    url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/USD/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status != 200:
                await message.answer("eror")
                return

            data = await response.json()
    rate = data[0]["Rate"]
    date = data[0]["Date"]

    text = (
        "AQSh dollari kursi\n"
        f"1 USD = {rate}\n"
        f"Date: {date}"
    )
    await message.answer(text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())