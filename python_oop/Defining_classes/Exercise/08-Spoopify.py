class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = songs
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"cannot add {song.name}. It's single"
        elif self.published:
            return "Cannot add songs. Album in published"
        elif song in [s for s in self.songs]:
            return "Song is already in the album"
        else:
            self.songs += (song,)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [s for s in self.songs]:
            return "Song is not in the album"
        elif self.published:
            return "Cannot remove songs. Album is published"
        else:
            ll = [el for el in self.songs]
            ll.remove(song_name)
            self.songs = tuple(ll)
            return f"Removed {song_name} from album {self.name}"

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published"
        self.published = True
        return f"Album {self.name} has been published"

    def details(self):
        new_line = '\n'
        return f"Album {self.name}\n" \
               f"{f'{new_line}'.join([f'== {s.get_info()}' for s in self.songs])}"


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.published = bool

    def add_album(self, album: Album):
        if album not in [a for a in self.albums]:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album}"
        return f"Band {self.name} already has {album} in their library"

    def remove_album(self, album_name: str):
        if self.published():
            return ""


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
