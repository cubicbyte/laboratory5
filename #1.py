class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

class Library:
    books = []

    def addBook(self, book):
        self.books.append(book)
    
    def removeBook(self, book):
        self.books.remove(book)

    def searchByAuthor(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books
    
    def searchByYear(self, year):
        books = []
        for book in self.books:
            if book.year == year:
                books.append(book)
        return books

    def searchByGenre(self, genre):
        books = []
        for book in self.books:
            if book.genre == genre:
                books.append(book)
        return books

def main():
    library = Library()

    library.addBook(Book('Марк Твен', 'Пригоди Тома Сойєра', 1876, 'роман'))
    library.addBook(Book('Джон Чейз', 'Помилка Тоні Вендіса', 1981, 'детектив'))
    library.addBook(Book('Стівен Хокінг', 'Коротка історія часу', 1988, 'фантастика'))

    author = 'Стівен Хокінг'
    books = library.searchByAuthor(author)
    if len(books) == 0:
        return
    book = books[0]

    print('Кількість книг автора ' + author, len(books))
    print('Автор книги', author)
    print('Титул книги', book.title)

    library.removeBook(book)
    books = library.searchByAuthor(author)
    print('Нова кількість книг автора ' + author, len(books))

if __name__ == '__main__':
    main()