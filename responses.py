import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def handle_response(message) -> str:
    p_message = message.lower()

    if(p_message=='hola'):
        return 'Hola!'
    if(p_message=='random'):
        return str(random.randInt(1,6))
    if(p_message=='!help'):
        return 'Aqui va la ayuda...'

    return 'No te entendí :('
