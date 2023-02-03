import sys
import time
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def handle_response(message) -> str:
    p_message = message.lower()

    if(p_message=='hola'):
        return 'Hola!'
    if(p_message=='random'):
        return str(random.randint(1,6))
    if(p_message=='help'):
        return 'Aqui va la ayuda...'

    return 'No te entendí :('

def getURLartistImage(artist_name) -> str:
    try:

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
    except Exception as e:
        return e
