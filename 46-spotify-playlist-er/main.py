from bs4 import BeautifulSoup
import requests
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")

selected_date = input(
    "Spotify time travel is what you want? Hmm.. sure! Give me a date in YYYY-MM-DD format. "
)

response = requests.get(f"{URL}/{selected_date}")
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "html.parser")
song_name_spans = soup.find_all(
    "span", class_="chart-element__information__song text--truncate color--primary"
)
song_names = [song.getText() for song in song_name_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = selected_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{selected_date} Billboard 100", public=False
)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
