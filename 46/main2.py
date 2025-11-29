import spotipy
from spotipy.oauth2 import SpotifyOAuth
from data import *

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                    client_id=SPOTIPY_CLIENT_ID,
                    client_secret=SPOTIPY_CLIENT_SECRET,
                    redirect_uri=SPOTIPY_REDIRECT_URI,
                    show_dialog=True,
                    username=USERNAME,
                    scope=scope))

user_id = sp.current_user()["id"]

song_names = []
with open("new.txt") as f:
    for line in f.readlines():
        song_names.append(line.strip())

song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)