class Book():
    def __init__(self, title, author, year_of_pubication=int):
        self._title = title.title()
        self._author = author
        self._year_of_publication = year_of_pubication
        self._available = True

    def __str__(self):
        return f'{self._author} autor(a) do livro {self._title} que foi publicado no ano {self._year_of_publication} que está {self._available}'

    def lend(self):
        self._available = False

    @staticmethod
    def verify_avaliable(year):
        available_books = [
            book for book in Book.books if book._year_of_publication == year and book._available]

        return available_books
