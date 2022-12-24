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
    ["Carlos Alberto", "carlosalberto@mail.com", "vanillacreamapplepie456"],
    ["adventurer_123", "adventurer123@gmail.com", "exploretheworld"],
    ["galactic_guru", "galacticguru@yahoo.com", "starwarsfan"],
    ["bookworm_bob", "bookwormbob@outlook.com", "ilovereading"],
    ["cat_lover_123", "catlover123@hotmail.com", "katkittykatkat"],
    ["monteiroluis", "elmonteiro@gmail.com", "ham_baga"],
    ["bookworm_cait", "bookwormcait@outlook.com", "ilovebob"],
    ["cat_lover_123", "catlover123@gmail.com", "kittykatkat"],
    ["the_hiking_hobo", "thehikinghobo@yahoo.com", "lovetheoutdoors"]
]

for i in users:
    cur.execute(
        "INSERT INTO USERS (username, email, password) VALUES (%s, %s, %s)", (i[0], i[1], i[2]))
    conn.commit()


# Adicionamos seguidores

followers = [
    [1, 3],
    [2, 6],
    [3, 9],
    [4, 12],
    [5, 15],
    [6, 2],
    [7, 5],
    [8, 8],
    [9, 11],
    [10, 14],
    [11, 1],
    [12, 4],
    [13, 7],
    [14, 10],
    [15, 13],
    [1, 5],
    [2, 8],
    [3, 11],
    [4, 14],
    [5, 2],
    [6, 5],
    [7, 8],
    [8, 11],
    [9, 14],
    [10, 1]
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
    [7, "Summer Hits", "The hottest tracks of the season 2021", 1],
    [2, "Chill Vibes", "Relaxing tunes to unwind after a long day", 0],
    [3, "Party Playlist", "Only Bangers", 1],
    [3, "Romantic Dinner", "Smooth and sultry tracks for a romantic evening in", 0],
    [7, "Motivation", "NULL", 0],
    [12, "Work from Home", "Upbeat tracks to keep you motivated while working remotely", 0],
    [9, "Workout Mix 2.0", "High-energy tunes to power through your workout", 1],
    [14, "Classical Relaxation", "Soothing classical tracks for relaxation", 1],
    [15, "Indie Discoveries", "Fresh indie tracks to discover and enjoy", 0]
]

for i in playlists:
    cur.execute("INSERT INTO PLAYLISTS (user_id, playlist_name, description, is_public) VALUES (%s, %s, %s, %s)",
                (i[0], i[1], i[2], i[3]))
    conn.commit()


# E para terminar pomos umas musicas na playlist
import random
plp = []

for i in range(100):
    plp.append(0)


playlist = []
for i in range(100):
    playlist_id = random.randint(1, 14)
    music_id = random.randint(1, 772)
    plp[playlist_id] += 1
    entry = [playlist_id, music_id, plp[playlist_id]]
    playlist.append(entry)




for i in playlist:
    cur.execute(
        "INSERT INTO PLAYLIST_SONGS (playlist_id, song_id, position) VALUES (%s, %s, %s)", (i[0], i[1], i[2]))
    conn.commit()

if os.path.exists("dados.sql"):
    os.remove("dados.sql")

os.system("mysqldump --no-create-info -u root -p spotifer > dados.sql")



