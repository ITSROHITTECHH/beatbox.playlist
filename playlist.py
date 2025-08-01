class Song:
    def __init__(self, title, artist, duration):
        self.title = title          # Song title
        self.artist = artist        # Song artist
        self.duration = duration    # Duration in seconds

    def __str__(self):
        # Nicely formatted string when printing a Song
        return f"{self.title} by {self.artist} ({self.duration} sec)"


# Define a Playlist class that can hold multiple songs
class Playlist:
    def __init__(self, name):
        self.name = name            # Playlist name
        self.songs = []             # List to store Song objects

    def add_song(self, song):
        self.songs.append(song)     # Add a song to the playlist

    def __len__(self):
        # Return number of songs in playlist
        return len(self.songs)
    
    def __getitem__(self , index):
        # allow indexing like playlist [0]
        return self.songs[index]
    
    def __str__(self):
        Playlist_info += f"Playlist: {self.name} ({len(self)} songs)\n"
        for i, song in enumerate(self.songs, start=1):
            playlist_info += f"{i}. {song}\n"
        return playlist_info


    

    
        

