class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  # Increment the song count when a new song is created
        Song.add_to_genres(genre)  # Add the genre to the genres list if it's not already there
        Song.add_to_artists(artist)  # Add the artist to the artists list if it's not already there
        Song.add_to_genre_count(genre)  # Update genre count
        Song.add_to_artist_count(artist)  # Update artist count

