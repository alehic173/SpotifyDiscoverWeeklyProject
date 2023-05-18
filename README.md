# SpotifyWeeklyReleaseProject


The purpose of this project is to save the songs in the "Discover Weekly" playlist that spotify provides each week. Every week this playlist is updated, and the user loses access to the previous weeks' songs. Adding those songs to a different playlist each week will prevent this. 

This script connects to and uses the [Spotify API](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks).

Here is a quick overview on how this project was accomplished:

<br>
<br>

**The Plan**

Step One: The playlist ID is needed for access. Will use the [Request Playlist ID](https://developer.spotify.com/documentation/web-api/reference/get-playlist) to obtain the ID and [Get Playlist Items](https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks) to get the songs. 
