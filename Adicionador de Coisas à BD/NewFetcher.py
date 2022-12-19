import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pymysql
import os

conn = pymysql.connect(host='localhost', user='root',
                       password='root', charset='utf8', db='spotifer')
cur = conn.cursor()


client_id = "d9487b41917d49de84729fe37f07a2b1"
client_secret = "8579a610bf214dddac2ae3ab0e62b415"
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

albumdict = {}

artistas_file = open("playlists.txt", "r")
data = artistas_file.read()

pls_urls = data.split("\n")
artistas_file.close()

for playlist in pls_urls:
    result = sp.playlist_tracks(playlist)
    artist_name = result['items'][0]['track']['artists'][0]['name']

    cur.execute("INSERT INTO ARTISTS (artist_name) VALUES (%s) ", artist_name)
    conn.commit()
    id = cur.lastrowid

    for x in range(0, len(result['items'])):
        # se está num album ou é single
        album = result['items'][x]['track']['album']['album_type']

        if album == "album":
            album_name = result['items'][x]['track']['album']['name']  # nome do album
            # release date do album
            release_date = result['items'][x]['track']['album']['release_date']

            if album_name not in albumdict:
                cur.execute("INSERT INTO ALBUMS (Name, Artist, ReleaseDate) VALUES (%s, %s, %s)",
                            (album_name, id, release_date))
                conn.commit()
                album_id = cur.lastrowid
                albumdict[album_name] = album_id

            # nome do artista
            music_name = result['items'][x]['track']['name']  # nome
            duration = result['items'][x]['track']['duration_ms'] / \
                1000  # duração segundos

            cur.execute("INSERT INTO SONGS (Name, Artist, Album, Duration) VALUES (%s, %s, %s, %s) ",
                        (music_name, id, albumdict.get(album_name), duration))
            conn.commit()

        else:
            # nome do artista
            music_name = result['items'][x]['track']['name']  # nome
            duration = result['items'][x]['track']['duration_ms'] / \
                1000  # duração segundos

            cur.execute(
                "INSERT INTO SONGS (Name, Artist, Duration) VALUES (%s, %s, %s) ", (music_name, id, duration))
            conn.commit()


# Agora criamos uns users e colocamos na db

users = [
    ["Pedro Sousa", "sussypedro@mail.com", "ilovepizzarolls"],
    ["Ines Cardoso", "inescardi@mail.com", "lerolero24"],
    ["Rui Silva", "ruisilva@mail.com", "chocochips123"],
    ["Sofia Martins", "sofiamartins@mail.com", "bananacake567"],
    ["Joao Rodrigues", "joaorodrigues@mail.com", "strawberryshortcake999"],
    ["Ana Santos", "anasantos@mail.com", "mintchocolatechip87326"],
    ["Carlos Alberto", "carlosalberto@mail.com", "vanillacreamapplepie456"]
]

for i in users:
    cur.execute(
        "INSERT INTO USERS (username, email, password) VALUES (%s, %s, %s)", (i[0], i[1], i[2]))
    conn.commit()


# Adicionamos seguidores

followers = [
    [1, 2],
    [1, 4],
    [2, 1],
    [2, 3],
    [3, 1],
    [3, 2],
    [3, 4],
    [5, 6],
    [5, 7],
    [6, 1],
    [6, 3],
    [7, 5],
    [7, 6]
]

for i in followers:
    cur.execute(
        "INSERT INTO FOLLOWERS (user_id, artist_id) VALUES (%s, %s)", (i[0], i[1]))
    conn.commit()


# E criamos uma playlists

playlists = [
    [1, "A mimir", "Musicas para dormir", 1],
    [2, "Inserir Nome", "NULL", 0],
    [4, "Workout Motivation", "Upbeat tracks to get your heart rate up", 1],
    [5, "Road Trip Playlist", "A mix of pop and rock hits for long car rides", 0],
    [6, "Study Session", "Focus-boosting instrumental tracks", 0],
    [7, "Summer Hits", "The hottest tracks of the season", 1]
]

for i in playlists:
    cur.execute("INSERT INTO PLAYLISTS (user_id, playlist_name, description, is_public) VALUES (%s, %s, %s, %s)",
                (i[0], i[1], i[2], i[3]))
    conn.commit()


# E para terminar pomos umas musicas na playlist

playlist = [
    [1, 31, 1],
    [1, 19, 2],
    [1, 14, 3],
    [2, 17, 1],
    [2, 22, 2],
    [2, 8, 3],
    [6, 59, 1],
    [6, 23, 2],
    [6, 46, 3],
    [6, 70, 4],
    [2, 12, 4],
    [2, 31, 5],
    [2, 50, 6],
    [3, 3, 1],
    [3, 32, 2],
    [3, 55, 3],
    [3, 67, 4],
    [4, 1, 1],
    [4, 15, 2],
    [4, 27, 3],
    [5, 7, 1],
    [5, 29, 2],
    [5, 53, 3]
]

for i in playlist:
    cur.execute(
        "INSERT INTO PLAYLIST_SONGS (playlist_id, song_id, position) VALUES (%s, %s, %s)", (i[0], i[1], i[2]))
    conn.commit()

os.remove("dados.sql")
os.system("mysqldump --no-create-info -u root -p spotifer > dados.sql")



