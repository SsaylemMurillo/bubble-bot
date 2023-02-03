import sys
import time
import random
import spotipy
import json
from urllib import parse, request
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import pytz
import subprocess

help = '\n**bubble-bot**' + '\nTo use the bot commands you just have to use the # character' + '\n\n***Commands: ***\n\n```Interaction with members```\n__#wave__: bubble will wave at you :D.' + '\n__#random__: bubble will generate a random number for you, between 1 and 10.' + '\n__#random number-number2__: bubble will generate a random number for you, between number and number2.' + '\n__#help__: bubble will show you all the commands.' + '\n__#time country__: bubble will show you the datetime of the specified country.' + '\n__#joke__: bubble will show you a joke from the saved jokes B).' + '\n__#reminder__: bubble will show you a reminder for a specific date.' + '\n\n```Integration with spotify```' + '\n__#artist artistnamehere__:  bubble will show you the cover from the specified artist.' + '\n__#album albumnamehere__: bubble will show you the cover from the specified album.' + '\n__#album albumnamehere artistnamehere__: bubble will show you the cover from the specified album and the specified artist.' + '\n\n\nSSAYKOs important note:' + '\n> This a bot in development so, not all the functions are 100% functional and free of bugs or errors, and not all the ' + 'functions are finished yet, so, the commands you see in this page, are the commands that are working already. Thank you for using the bot.'

def handle_response(message_info, message):
    p_message = message.lower()
    values = ['No entendí tu petición D:']

    if(p_message=='wave'):
        values.clear()
        values.insert(0, 'Hola ' + f'{message_info.author.mention}')
        values.insert(1, handle_random_gif())
    if(p_message.startswith('random')):
        values.clear()
        mystring = split_from_a_string(p_message, word)
        values.insert(0, str(random.randint()))
    if(p_message=='help'):
        values.clear()
        values.insert(0, help)

    return values

def create_random_integer(message) -> str:
    random_number = 'Tu numero aleatorio es: '
    if (len(message)>0):
        p_message = message.lower()
        p_message = p_message.split('-')
        random_number += str(random.randint(int(p_message[0]),int(p_message[1])))
    else:
        random_number += str(random.randint(1,10))
    return random_number

def getURLartistImage(artist_name) -> str:
    try:
        if(artist_name != ''):
            auth_manager = SpotifyClientCredentials()
            sp = spotipy.Spotify(auth_manager=auth_manager)

            name = artist_name.lower()

            results = sp.search(q='artist:' + name, type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                artist = items[0]
                return artist['images'][0]['url']
            else:
                return 'Error'
        else:
            return Exception
    except Exception as e:
        return e


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

def handle_random_gif():
    url = "http://api.giphy.com/v1/gifs/random"

    params = parse.urlencode({})

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())

    image = data['data']['images']['original']['mp4']

    return image

#
#def handle_download_audio_URL(url):
#    youtube-dl.exe -f bestaudio linkdelvideo
#    completed = subprocess.run([""])