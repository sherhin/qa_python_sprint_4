import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    """Фикстура возвращает экземпляр класса"""
    return BooksCollector()
