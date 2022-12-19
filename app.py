import db
import logging
from flask import abort, render_template, Flask
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

APP = Flask(__name__)


@APP.route('/')
def index():
    stats = {}
    x = db.execute('SELECT COUNT(*) AS artist1 FROM ARTISTS').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS song1 FROM SONGS').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS album1 FROM ALBUMS').fetchone()
    stats.update(x)
    logging.info(stats)
    return render_template('index.html', stats=stats)


# Songs
@APP.route('/songs/')
def list_songs():
    songs = db.execute(
        '''
      SELECT song_id, Name, Artist, Album, Duration 
      FROM SONGS
      ORDER BY song_id
      ''').fetchall()
    return render_template('songs-list.html', SONGS=songs)


@APP.route('/songs/<int:id>/')
def get_song(id):
    song = db.execute(
        '''
      SELECT song_id, Name, Artist, Duration , Album
      FROM SONGS
      WHERE song_id = %s
      ''', id).fetchone()
    artist = db.execute(
        '''
      SELECT artist_id, artist_name
      FROM ARTISTS
      WHERE artist_id = %s
      ''', song["Artist"]).fetchone()

    album = {"Name": "Não pertence a um album."}

    if song["Album"] != None:
        album = db.execute(
            '''
        SELECT album_id, Name, Artist, ReleaseDate
        FROM ALBUMS
        WHERE album_id = %s
        ''', song["Album"]).fetchone()

    if song is None:
        abort(404, 'Song ID {} does not exist.'.format(id))

    return render_template('song.html',
                           song=song, artist=artist, album=album)

# Songs


@APP.route('/albums/<int:id>/')
def list_album_songs(id):
    album = db.execute(
        '''
        SELECT album_id, Name, Artist, ReleaseDate
        FROM ALBUMS
        WHERE album_id = %s
        ''', id).fetchone()
    song = db.execute(
        '''
        SELECT song_id, Name, Artist, Duration , Album
        FROM SONGS
        WHERE Album = %s
        ''', id).fetchall()
    logging.info(song)

    artist = db.execute(
        '''
      SELECT artist_id, artist_name
      FROM ARTISTS
      WHERE artist_id = %s
      ''', album["Artist"]).fetchone()

    return render_template('album.html', album=album, SONGS=song, artist=artist)


@APP.route('/albums-list/')
def list_albums():
    album = db.execute(
        '''
      SELECT album_id, Name, Artist
      FROM ALBUMS
      ORDER BY album_id
      ''').fetchall()
    return render_template('albums-list.html', ALBUMS=album)

@APP.route('/artist/<int:id>/')
def artist(id):
    artist = db.execute(
        '''
      SELECT artist_id, artist_name
      FROM ARTISTS
      WHERE artist_id = %s
      ''', id).fetchone()
    album = db.execute(
        '''
      SELECT album_id, Name, Artist
      FROM ALBUMS
      WHERE Artist = %s
      ''', id).fetchall()
    
    return render_template('albums-list.html', ALBUMS=album, artist=artist)

@APP.route('/artists-list/')
def list_artists():
    artists = db.execute(
        '''
      SELECT artist_id, artist_name 
      FROM ARTISTS
      ORDER BY artist_id
      ''').fetchall()
    return render_template('artists-list.html', ARTISTS=artists)