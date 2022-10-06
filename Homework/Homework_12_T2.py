class Author:
    def __init__(self, name, country, birthday, books=None):
        self.name = name
        self.country = country
        self.birthday = birthday

        self.books = [] if books is None else books


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author name={self.name} country={self.country} birthday={self.birthday}>"

class Book:
    number_of_books = 0

    def __init__(self, name, year, author):
        if not isinstance(author, Author):
            raise ValueError("The author should be an instance of Author class")

        self.name = name
        self.year = year
        self.author = author

        Book.number_of_books += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Book name={self.name} year={self.year} author={self.author}>"

class Library:
    def __init__(self, name, books=None, authors=None):
        self.name = name
        self.books = [] if books is None else books
        self.authors = [] if authors is None else authors

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"<Library name={self.name}>"

        def new_book(self,name, year, author):
            book = Book(name, year, author)

            self.books.append(book)

            return book

        def filter_by_author(self,author):
            if not isinstance(author, Author):
                raise ValueError("The author should be an instance of Author class")

            def author_filter(book):
                return book.author == author

            return list(filter(author_filter, self.books))

        def group_by_year(self, year):
                return list(filter(lambda book: book.year == year, self.books))

    def main():
        library = Library("First National Library")

        author1 = Author("Yval Noah Harari", "Israel", "24 Feb 1976", "Sapiens: A Brief History of Humankind")
        book1 = library.new_book("Sapiens: A Brief History of Humankind", 2011, author1)
        print(repr(author1))
        print(library.group_by_year(2011))

        author1_2 = Author("Yuval Noah Harari", "Israel", "24 Feb 1976", "Homo Deus")
        book2 = library.new_book("Homo Deus", 2015, author1_2)
        print(repr(author1_2))
        print(library.group_by_year(2015))

        print("Total number of books:", Book.number_of_books)
    
    if __name__ == "__main__":
        main()



