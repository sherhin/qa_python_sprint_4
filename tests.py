import pytest

from main import BooksCollector

BOOKS_AND_GENRES = {
    'Фантастика': ['Марсианские хроники', 'Дюна'],
    'Ужасы': ['Оно', 'Мертвая зона', 'Кладбище домашних животных'],
    'Детективы': ['Восточный экспресс'],
    'Мультфильмы': ['Золушка', 'Красавица и чудовище'],
    'Комедии': ['Автостопом по Галактике', 'Трое в лодке не считая собаки', 'Дживс и Вустер']
}

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.mark.usefixtures('collector')
class TestBooksCollector:

    @staticmethod
    def add_new_book(collector, name):
        """Метод добавляет книгу в список и проверяет ее наличие
        """
        collector.add_new_book(name)
        books = collector.get_books_genre().keys()
        return name in books

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_check_in_books(self, collector):
        """Проверяем добавление новой книги
        """
        book = self.add_new_book(collector, name='Тайная история')
        assert book

    def test_add_new_book_too_long_name_negative(self, collector):
        """Проверяем добавление новой книги с названием > 41 символа
        """
        book = 'Книга с очень, очень, очень, очень, очень, очень, очень длинным названием'
        book = self.add_new_book(collector, name=book)
        assert not book

    def test_add_new_book_without_name_negative(self, collector):
        """Проверяем добавление новой книги с названием < 0 символов
        """
        book = self.add_new_book(collector, name='')
        assert not book

    def test_add_new_book_check_empty_genre(self, collector):
        """Проверяем, что у добавленной книги жанр пуст
        """
        book = 'Джентльмены и игроки'
        self.add_new_book(collector, name=book)
        assert collector.get_book_genre(book) == ''

    def test_set_book_genre_from_list_check_genre(self, collector):
        """Проверяем установку книге жанра
        """
        book = 'Оно'
        genre = 'Ужасы'
        assert genre in collector.genre
        collector.add_new_book(book)
        self.add_new_book(collector, name=book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == 'Ужасы'

    def test_set_book_genre_not_in_list_negative(self, collector):
        """Проверяем, установки книге жанра не из списка жанров
        """
        book = 'Мизери'
        genre = 'Триллер'
        self.add_new_book(collector, name=book)
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
    #     'books, genre, count', (
    #         (['Марсианские хроники', 'Дюна'], 'Фантастика', 2),
    #         (['Оно', 'Мертвая зона', 'Кладбище домашних животных'], 'Ужасы', 3),
    #         (['Восточный экспресс'], 'Детективы', 1),
    #         (['Золушка', 'Красавица и чудовище'], 'Мультфильмы', 2),
    #         (['Трое в лодке не считая собаки', 'Дживс и Вустер', 'Автостопом по Галактике'], 'Комедии', 3)
    #     )
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
        """Проверяем, изменение жанра книги
        """
        book = 'Автостопом по Галактике'
        genre = 'Комедии'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        book_genre = collector.get_book_genre(book)
        assert book_genre == genre
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
        book_genre = collector.get_book_genre(book)
        assert book_genre == genre
        new_genre = 'Триллеры'
        collector.set_book_genre(book, new_genre)
        book_genre = collector.get_book_genre(book)
        assert book_genre == genre


    def test_get_books_for_children(self, collector):
        for genre, books in BOOKS_AND_GENRES.items():
            for book in books:
                collector.add_new_book(book)
                collector.set_book_genre(book, genre)
        books_for_children = collector.get_books_for_children()
        for book in books_for_children:
            assert collector.get_book_genre(book) not in collector.genre_age_rating







