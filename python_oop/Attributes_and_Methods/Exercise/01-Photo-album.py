from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        matrix = []
        for i in range(pages):
            line = [] * 4
            matrix.append(line)
        self.photos = matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count / 4
        return cls(ceil(pages))

    def add_photo(self, label: str):
        photos = len([len(el) for el in self.photos])
        if photos < self.pages * 4:
            for i in range(len(self.photos)):
                if len(self.photos[i]) < 4:
                    self.photos[i].append(label)
                    return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        else:
            return 'No more free spots'

    def display(self):
        result = []
        page_separation = "-----------"
        for i in range(self.pages):
            result.append(page_separation)
            row = ('[] ' * len(self.photos[i])).rstrip()
            result.append(row)
        result.append(page_separation)
        return "\n".join(result) + '\n'



album = PhotoAlbum(2)

print(album.add_photo('baby'))
print(album.add_photo('first grade'))
print(album.add_photo('eight grade'))
print(album.add_photo('party with friends'))
print(album.photos)
print(album.add_photo('prom'))
print(album.add_photo('wedding'))
print(album.display())