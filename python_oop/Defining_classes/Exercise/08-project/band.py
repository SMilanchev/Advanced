from typing import List
from .album import Album


class Band:
    name: str
    albums: List[Album]

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album.name in map(lambda a: a.name, self.albums):
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        album_names = [s.name for s in self.albums]
        if album_name not in album_names:
            return f"Album {album_name} is not found."
        album = self.albums[album_names.index(album_name)]
        if album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        band_info = [f"Band {self.name}"]
        album_info = [
            a.details() for a in self.albums
        ]
        return "\n".join(band_info+album_info)