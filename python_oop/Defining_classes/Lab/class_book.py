from dataclasses import dataclass


@dataclass()
class Book:
    name: str
    author: str
    pages: int


book = Book("My Book", "Me", 200)

print(book.name)
print(book.author)
print(book.pages)