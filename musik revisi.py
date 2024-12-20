import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API credentials
client_id = '035132c66a2a4238af489768bf6477fb'
client_secret = 'bad4e798be2749b19889b59938985564'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_tracks(mood, genre, limit):
    query = f"{mood} genre:{genre}" if genre else mood
    results = sp.search(q=query, type='track', limit=limit)
    tracks = results['tracks']['items']
    track_list = []
    for track in tracks:
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'preview_url': track['preview_url']
        }
        track_list.append(track_info)
    return track_list

def display_tracks(tracks):
    for track in tracks:
        print(f"\nTrack: {track['name']}, \nArtist: {track['artist']}, \nAlbum: {track['album']}, \nRelease Date: {track['release_date']}, \nPreview: {track['preview_url']}")
        print("-" * 50)  # Garis pemisah
    print()

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # 1.untuk menginput username dan password

    while True:
        mood = input("Enter your mood (happy, sad, energetic, etc, or enter an artist name) or 'exit' to quit: ")
        if mood.lower() == 'exit':
            break

        if not mood:
            print("Please enter a mood or an artist name.")
            continue

        genre = input("Enter a genre (optional, press enter to skip): ")
        
        try:
            limit = int(input("Enter the number of tracks to display: "))
            if limit <= 0:
                print("Please enter a number greater than 0.")  # 2. untuk set limit tidak bisa 0
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        tracks = get_tracks(mood, genre, limit)
        display_tracks(tracks)

        another_search = input("Would you like to search for more recommendations? (yes/no): ").lower() # 3. setelah diberikan rekomendasi pengguna diberikan pilihan untuk mencari rekomendasi lain atau keluar
        if another_search != 'yes':
            break

if __name__ == "__main__":
    main()
