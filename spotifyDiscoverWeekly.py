# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:03:42 2023

@author: alexa
"""

import spotipy 
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect

# Flask will allow for storing the OAuth 
# user will only have to authorize once and will stay signed in
flask_app = Flask(__name__)

flask_app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
# Prevents unauthorized access to the cookie
flask_app.secret_key = 'sd97s9f79sdfu8g@*(&^Fs'

TOKEN_info = 'token_info'

@flask_app.route('/')
def login():
    # Generates authorization url
    auth_url = create_oauth().get_authorize_url()
    # redirect user to external url
    return redirect(auth_url)
    
@flask_app.route('/redirect')
def redirect_page():
    # clear existing sessions so that existing user data is cleared
    session.clear()
    code = request.args.get('code')
    # exchanges auth code for access token that will be stored in token_info var
    token_info = create_oauth().get_access_token(code)
    # store token_info in session
    session[TOKEN_info] =  token_info
    return redirect(url_for('save_discover_weekly', external = True))
    

@flask_app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    
    # try to get token information
    try:
        token_info = get_token()
    except:
        print('User not logged in')
        # redirect user back to home page
        return redirect('/')
    
    # create Spotipy instance with access token
    sp = spotipy.Spotify(auth=token_info['access_token'])
    saved_weekly_playlist_id = None
    discover_weekly_playlist_id = None
    username = sp.current_user()['id']
    
    # calls api endpoint Current User Playlist
    # Get all playlists
    current_playlists = sp.current_user_playlists()['items']
    
    # loop through playlists to get Discover Weekly ID and Saved Weekly (new playlist) id
    for playlist in current_playlists:
        if( playlist['name'] == "Discover Weekly"):
            discover_weekly_playlist_id = playlist['id']
        if (playlist['name'] == "Saved Weekly"):
            saved_weekly_playlist_id = playlist['id']
   
    
    # check if playlists exist. If Saved Weekly playlist does not exist, create it
    if not discover_weekly_playlist_id:
        return 'Discover Weekly Playlist Not Found'
    if not saved_weekly_playlist_id:
        new_playlist = sp.user_playlist_create(username, 'Saved Weekly', True)
        saved_weekly_playlist_id = new_playlist['id']
    
    # get songs of discover weekly playlist
    discover_weekly_playlist = sp.playlist_items(discover_weekly_playlist_id)
    
    song_uris = []
    # Create list of song uris from discover weekly playlist
    for song in discover_weekly_playlist['items']:
        
        song_uri = song['track']['uri']
        song_uris.append(song_uri)
    
    sp.user_playlist_add_tracks(username,saved_weekly_playlist_id, song_uris)
        
        
    return "SUCCESS!!!!!!!!"
    
# function to get token info when needed
def get_token():
    token_info = session.get(TOKEN_info, None)
    # if token doesn't exist
    if not token_info:
        redirect(url_for('login', external=False))

    # check if token is expired
    now = int(time.time())
    is_expired = token_info['expires_at']-now <60
    
    # if expired, create new oauth
    if(is_expired):
        spotify_oauth = create_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info
    
# Create the spotify OAuth

# def create_oauth():
#     return SpotifyOAuth(client_id = 'INSERT CLIENT ID', client_secret = 'INSERT SECRET ID',
#                         redirect_uri = url_for('redirect_page', _external=True), 
#                         scope = 'user-library-read playlist-modify-public playlist-modify-private')


flask_app.run(debug=True)
