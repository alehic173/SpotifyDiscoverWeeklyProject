# SpotifyDiscoverWeeklyProject


The purpose of this project is to save the songs in the "Discover Weekly" playlist that spotify provides each week using **Python**. Every week this playlist is updated, and the user loses access to the previous weeks' songs. Adding those songs to a different playlist each week will prevent this. 

This script connects to and uses the [Spotify API](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks).

Here is a quick overview on how this project was accomplished:

<br>
<br>

**Overall Plan**
<br>
<br>
Step One: Implement OAuth to have the users permission to modify the playlsit and make changes. 
<br>
<br>
Step Two: The playlist ID is needed for access. Will use the [Request Playlist ID](https://developer.spotify.com/documentation/web-api/reference/get-playlist) to obtain the ID and [Get Playlist Items](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks) to get the songs.
<br>
<br>
Step Three: Add list of songs to a new playlist. First, need to check that the new playlist exists. If it exists, obtain the playlist ID. If not, create the playlist using the [Create Playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist) request. [Add Items to Playlist](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist) will be used to add the songs to the playlist. 
<br>
<br>
Step Four: List Discover Weekly track uris and save them to a list. Take that list and add to save weekly playlist.
<br>
<br>
<br>
Necessary Beginning Steps
<br>
a  Create app in spotify for developers [dashboard](https://developer.spotify.com/dashboard)
<br>
b  modify redirect url to match server http... +'/redirect'
