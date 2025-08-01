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
        self.songs = [] 