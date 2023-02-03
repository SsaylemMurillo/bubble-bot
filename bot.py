import discord
import os
import responses
from PIL import Image
import requests
from io import BytesIO
import aiohttp
import discord


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def search_artist_image(message, user_message, is_private):
    try:
        response = responses.getURLartistImage(user_message)
        img = create_image_from_URL(response)
        img = img.save('savedimage.jpeg')
        await message.channel.send(file=discord.File('savedimage.jpeg'))
        os.remove('savedimage.jpeg')
    except Exception as e:
        print(e)

def create_image_from_URL(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


def run_discord_bot(token) -> str:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '#':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '$':
            user_message = user_message[1:]
            await search_artist_image(message, user_message, is_private=False)
    client.run(token)