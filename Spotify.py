import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these values with your own
CLIENT_ID = 'your client id'
CLIENT_SECRET = 'your client secret'
REDIRECT_URI = 'http://localhost:8888/callback'

# Scope for managing playlists
SCOPE = 'playlist-modify-public playlist-modify-private'

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Test authentication
print(sp.current_user())

# List of artist names
artists = [
    'Zinoleesky',
    'Wizkid',
    'Asake',
    'Wande Coal',
    'Ariana Grande'
]

# Create a playlist
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, 'Top Hits Playlist', public=True)
playlist_id = playlist['id']

print(f"Created playlist with ID: {playlist_id}")

# Function to get top tracks for an artist
def get_top_tracks(artist_name, limit=7):
    # Search for the artist
    result = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    if result['artists']['items']:
        artist_id = result['artists']['items'][0]['id']
        # Get top tracks for the artist
        top_tracks = sp.artist_top_tracks(artist_id)
        # Fetch only the specified number of tracks
        return [track['uri'] for track in top_tracks['tracks'][:limit]]
    return []

# Retrieve top tracks for each artist and add to the playlist
track_uris = []
for artist in artists:
    print(f"Fetching top tracks for {artist}...")
    top_tracks = get_top_tracks(artist, limit=7)  # Fetch exactly 7 tracks
    if top_tracks:
        track_uris.extend(top_tracks)
    else:
        print(f"No tracks found for {artist}.")

# Add tracks to the playlist
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"Added {len(track_uris)} tracks to the playlist.")
else:
    print("No tracks to add.")

# Print the playlist URL
playlist_url = playlist['external_urls']['spotify']
print(f"Playlist created: {playlist_url}")