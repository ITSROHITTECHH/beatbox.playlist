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
        # Nicely formatted string when printing a Playlist
        playlist_info = f"Playlist: {self.name} ({len(self)} songs)\n"
        for i, song in enumerate(self.songs, start=1):
            playlist_info += f"{i}. {song}\n"
        return playlist_info
    
    def __add__(self, other):
        # Combine two playlists using the + operator
        combined = Playlist(f"{self.name} + {other.name}")
        combined.songs = self.songs + other.songs
        return combined

# Create some Song objects

song1 = Song("angreji beat", "yoyo honey singh", 200)
song2 = Song("jee ni lagda", "karan aujla ", 180)
song3 = Song("gendaphool", "badshah", 195)
song4 = Song("blue eyes", "yoyo honey singh", 225)
song5 = Song("i am disco dancer", "vijay benedict", 220)
song6 = Song("meri umar ke no jawano", "kishore kumar", 290)
song7 = Song("A billinare", "yo yo honey singh", 160)
song8 = Song("softly", "karan aujla", 180)
song9 = Song("nature", "kabira", 200)
song10 = Song("excusses", "ap dhillon ", 210)
# love songs
song11 = Song("tum hi ho", "arjit singh", 240)
song12= Song("Pehle bhi main", "vishal mishra", 245)
song13= Song("Shape of You", "Ed Sheeran", 240)
song14= Song("o saajna", "akhil sachdeva", 197)
song15= Song("ae dil hai mushkil", "arjit singh", 210)
song16= Song("bulleya", "amit mishra", 205)
song17= Song("teri jhuki nazar", "shafqat amanat ali", 220)
song18= Song("saiyaara", "faheem abdullah", 290)
song19= Song("teri meri kahani", "arjit singh", 230)
song20= Song("maahi", "sharib toshi", 215)



# Create two Playlists and add songs

pop_hits = Playlist("Pop Hits")
pop_hits.add_song(song1)
pop_hits.add_song(song2)
pop_hits.add_song(song3)
pop_hits.add_song(song4)
pop_hits.add_song(song5)
pop_hits.add_song(song6)
pop_hits.add_song(song7)
pop_hits.add_song(song8)
pop_hits.add_song(song9)
pop_hits.add_song(song10)

love_songs = Playlist("Love Songs")
love_songs.add_song(song11)
love_songs.add_song(song12)
love_songs.add_song(song13)
love_songs.add_song(song14)
love_songs.add_song(song15)
love_songs.add_song(song16)
love_songs.add_song(song17)
love_songs.add_song(song18)
love_songs.add_song(song19)
love_songs.add_song(song20)



# Print individual playlists

print(pop_hits)
print(love_songs)

# Combine playlists using + operator (__add__)

combined = pop_hits + love_songs
print(combined)

# Get the number of songs using len()

print(f"Total songs in combined playlist: {len(combined)}")

# Access a song using index (__getitem__)

print(f"First song: {combined[0]}")


    

    
        

