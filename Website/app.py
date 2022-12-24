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
    x = db.execute('SELECT COUNT(*) AS user1 FROM USERS').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS playlist1 FROM PLAYLISTS').fetchone()
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


@APP.route('/albums/<int:id>/')
def list_album_songs(id):
    album = db.execute(
        '''
        SELECT album_id, Name, Artist, ReleaseDate
        FROM ALBUMS
        WHERE album_id = %s
        ''', id).fetchone()

    if album is None:
        abort(404, 'Album ID {} does not exist.'.format(id))

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

    if artist is None:
          abort(404, 'Artist ID {} does not exist.'.format(id))

    album = db.execute(
        '''
      SELECT album_id, Name, Artist
      FROM ALBUMS
      WHERE Artist = %s
      ''', id).fetchall()

    stats = {}
    x = db.execute('SELECT COUNT(*) AS numfollowers FROM FOLLOWERS where artist_id = %s', id).fetchone()
    stats.update(x)

    song = db.execute(
        '''
      SELECT song_id, Name, Duration, Album
      FROM SONGS
      WHERE Artist = %s AND Album IS NULL
      ''', id).fetchall()
    
    logging.info(song)

    return render_template('artist.html', ALBUMS=album, artist=artist, followers=stats, SONGS=song)

@APP.route('/artists-list/')
def list_artists():
    artists = db.execute(
        '''
      SELECT artist_id, artist_name 
      FROM ARTISTS
      ORDER BY artist_id
      ''').fetchall()
    return render_template('artists-list.html', ARTISTS=artists)


@APP.route('/users-list/')
def list_users():
    users = db.execute(
        '''
      SELECT user_id, username, email, password
      FROM USERS
      ORDER BY user_id
      ''').fetchall()
    return render_template('users-list.html', USERS=users)


@APP.route('/playlists-list/')
def list_playlsits():
    playlists = db.execute(
        '''
      SELECT playlist_id, playlist_name, user_id, description, is_public
      FROM PLAYLISTS
      ORDER BY playlist_id
      ''').fetchall()
    return render_template('playlists-list.html', PLAYLISTS=playlists)


@APP.route('/playlist/<int:id>/')
def list_playlist_songs(id):
    playlist = db.execute(
        '''
      SELECT playlist_id, playlist_name, user_id, description, is_public
      FROM PLAYLISTS
      WHERE playlist_id = %s
      ''', id).fetchone()

    if playlist is None:
        abort(404, 'Playlist ID {} does not exist.'.format(id))
      
    asong = db.execute(
        '''
        SELECT playlist_id, song_id, position, Name, Duration
        FROM PLAYLIST_SONGS NATURAL JOIN SONGS
        WHERE playlist_id = %s
        ''', id).fetchall()

    user = db.execute(
        '''
      SELECT user_id, username
      FROM USERS
      WHERE user_id = %s
      ''', playlist["user_id"]).fetchone()

    return render_template('playlist.html', playlist=playlist, SONGS=asong, user=user)


@APP.route('/user/<int:id>/')
def user(id):
    aartist = db.execute(
        '''
      SELECT user_id, artist_id, artist_name
      FROM FOLLOWERS NATURAL JOIN ARTISTS
      WHERE user_id = %s
      ''', id).fetchall()

    playlist = db.execute(
        '''
      SELECT playlist_id, playlist_name, user_id, description, is_public
      FROM PLAYLISTS
      WHERE user_id = %s
      ''', id).fetchall()

    user = db.execute(
        '''
      SELECT user_id, username, email, password
      FROM USERS
      WHERE user_id = %s
      ''', id).fetchone()

    if user is None:
        abort(404, 'User ID {} does not exist.'.format(id))
    
    return render_template('user.html', user=user, ARTISTS=aartist, PLAYLISTS=playlist)


@APP.route('/artists-list/search/<expr>/')
def search_artist(expr):
  expr = '%' + expr + '%'
  artists = db.execute(
      ''' 
      SELECT artist_id, artist_name
      FROM ARTISTS 
      WHERE artist_name LIKE %s
      ''', expr).fetchall()
  return render_template('artists-list.html', ARTISTS=artists)

@APP.route('/songs/search/<expr>/')
def search_song(expr):
  expr = '%' + expr + '%'
  songs = db.execute(
      ''' 
      SELECT song_id, Name, Artist, Album, Duration 
      FROM SONGS
      WHERE Name LIKE %s
      ''', expr).fetchall()
  return render_template('songs-list.html', SONGS=songs)

@APP.route('/albums-list/search/<expr>/')
def search_album(expr):
  expr = '%' + expr + '%'
  album = db.execute(
      ''' 
      SELECT album_id, Name, Artist
      FROM ALBUMS
      WHERE Name LIKE %s
      ''', expr).fetchall()
  return render_template('albums-list.html', ALBUMS=album)

@APP.route('/users-list/search/<expr>/')
def search_user(expr):
  expr = '%' + expr + '%'
  user = db.execute(
      ''' 
      SELECT user_id, username, email, password
      FROM USERS
      WHERE username LIKE %s
      ''', expr).fetchall()
  return render_template('users-list.html', USERS=user)


@APP.route('/playlists-list/search/<expr>/')
def search_playlist(expr):
  expr = '%' + expr + '%'
  playlist = db.execute(
      ''' 
      SELECT playlist_id, playlist_name, user_id, description, is_public
      FROM PLAYLISTS
      WHERE Name LIKE %s
      ''', expr).fetchall()
  return render_template('albums-list.html', PLAYLISTS=playlist)