import pytest

from data import BOOKS_AND_GENRES


@pytest.mark.usefixtures('collector')
class TestBooksCollector:

    @staticmethod
    def add_new_book(collector, name):
        """Метод добавляет книгу в список и проверяет ее наличие
        """
        collector.add_new_book(name)
        books = collector.get_books_genre().keys()
        return name in books

    def test_add_new_book_check_in_books(self, collector):
        """Проверяем добавление новой книги
        """
        book = self.add_new_book(collector, name='Тайная история')
        assert book

    @pytest.mark.parametrize(
        'name', ['Книга с очень, очень, очень, очень, очень, очень, очень длинным названием', '']
    )
    def test_add_new_book_name_validation_negative(self, collector, name):
        """Проверяем добавление новой книги с названием > 41 символа и < 0
        """
        book_name = name
        book = self.add_new_book(collector, book_name)
        assert not book

    def test_add_new_book_check_empty_genre(self, collector):
        """Проверяем, что у добавленной книги жанр пуст
        """
        book = 'Джентльмены и игроки'
        self.add_new_book(collector, book)
        assert collector.get_book_genre(book) == ''

    def test_set_book_genre_from_list_check_genre(self, collector):
        """Проверяем установку книге жанра
        """
        book = 'Оно'
        genre = 'Ужасы'
        collector.add_new_book(book)
        self.add_new_book(collector, book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == 'Ужасы'

    def test_set_book_genre_not_in_list_negative(self, collector):
        """Проверяем, установки книге жанра не из списка жанров
        """
        book = 'Мизери'
        genre = 'Триллер'
        self.add_new_book(collector, book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_book_not_exists_negative(self, collector):
        """Проверяем, установки книге жанра для несуществующей книги
        """
        book = 'Тайное окно'
        collector.set_book_genre(book, 'Детектив')
        genre = collector.get_book_genre(book)
        assert genre is None

    @pytest.mark.parametrize(
        'genre, books', (BOOKS_AND_GENRES.items())
    )
    def test_get_book_with_specific_genre(self, collector, genre, books):
        """Проверяем, получение книг по жанру
        """
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        genre_books = collector.get_books_with_specific_genre(genre)
        assert genre_books == books

    def test_get_book_with_specific_genre_not_exists_negative(self, collector):
        """Проверяем, получение книг по несуществующему жанру
        """
        genre_books = collector.get_books_with_specific_genre('Триллеры')
        assert len(genre_books) == 0

    def test_change_book_genre(self, collector):
        """Проверяем, изменение жанра книги"""
        book = 'Автостопом по Галактике'
        genre = 'Комедии'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        new_genre = 'Фантастика'
        collector.set_book_genre(book, new_genre)
        book_genre = collector.get_book_genre(book)
        assert book_genre == new_genre

    def test_change_book_genre_to_not_exists_negative(self, collector):
        """Проверяем, изменение жанра книги на несуществующий
        """
        book = 'Автостопом по Галактике'
        genre = 'Комедии'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        new_genre = 'Триллеры'
        collector.set_book_genre(book, new_genre)
        book_genre = collector.get_book_genre(book)
        assert book_genre != new_genre

    def test_get_books_for_children(self, collector):
        """Проверяем получение списка книг с жанрами для детей
        """
        for genre, books in BOOKS_AND_GENRES.items():
            for book in books:
                collector.add_new_book(book)
                collector.set_book_genre(book, genre)
        books_for_children = collector.get_books_for_children()

        for book in books_for_children:
            assert collector.get_book_genre(book) not in collector.genre_age_rating

    def test_add_book_in_favorites(self, collector):
        """Проверяем добавление книги в favorites
        """
        book = 'Тринадцатая сказка'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert book in favorites

    def test_add_book_in_favorites_book_not_exists_negative(self, collector):
        """Проверяем добавление книги в favorites
        """
        book = 'Дон Кихот'
        collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert book not in favorites

    def test_remove_book_from_favorites(self, collector):
        """Проверяем удаление книги из favorites
        """
        book = 'Тринадцатая сказка'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert book not in favorites

    def test_get_list_favorites(self, collector):
        """Проверяем получение заполненного списка favorites
        """
        expected_favorites_books = []
        favorites = collector.get_list_of_favorites_books()
        for books in BOOKS_AND_GENRES.values():
            for book in books:
                collector.add_new_book(book)
                collector.add_book_in_favorites(book)
                expected_favorites_books.append(book)
        assert favorites == expected_favorites_books
