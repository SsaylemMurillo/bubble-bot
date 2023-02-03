import discord
import os
import responses
import requests
from PIL import Image
import requests
from io import BytesIO
import aiohttp
import discord


async def send_message(message, user_message):
    try:
        response = responses.handle_response(message, user_message)
        # organizing the content of the responses
        myEmbed = discord.Embed(title='_Interacción con miembros_', description=response[0], color=discord.Color.random(),)
        # waiting to send it
        await message.channel.send(embed=myEmbed)
        if (len(response)>1):
            await message.channel.send(response[1])
        
    except Exception as e:
        print(e)

async def generate_random_integer_range(message, user_message):
    try:
        response = responses.create_random_integer(user_message)
        myEmbed = discord.Embed(title='_Interacción con miembros_', description=response, color=discord.Color.random())
        await message.channel.send(embed=myEmbed)
    except Exception as e:
        print(e)

async def search_artist_image(message, user_message):
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

def split_from_a_string(value:str, word:str) -> str:
        stringArray = value.split()
        newString = ''
        i = 0
        for x in stringArray:
            if (x == word):
                continue
            else:
                if (i==0):
                    newString+= x
                else:
                    newString+= ' ' + x
                i+=1
        return newString



def run_discord_bot(token) -> str:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        try:
            if message.author == client.user:
                return

            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            if user_message.startswith('#artist'):
                user_message = user_message[1:]
                user_message = split_from_a_string(user_message, 'artist')
                await search_artist_image(message, user_message)
            if user_message.startswith('#random'):
                user_message = user_message[1:]
                user_message = split_from_a_string(user_message, 'random')
                await generate_random_integer_range(message, user_message)
            elif user_message[0] == '#':
                user_message = user_message[1:]
                await send_message(message, user_message)
        except Exception as e:
            print(e)
    client.run(token)

        