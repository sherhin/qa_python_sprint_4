# qa_python

**Для класса BooksCollector реализованы следующие тесты:**

* Добавление книги: **test_add_new_book_check_in_books**
* Добавление книги с названием больше или меньше допустимого: **ttest_add_new_book_name_validation_negative**
* Добавление книги с пустым значением жанра: **test_add_new_book_check_empty_genre**
* Назначение книге жанра: **test_set_book_genre_from_list_check_genre**
* Назначение книге жанра не из списка: **test_set_book_genre_not_in_list_negative**
* Назначение жанра книге не из списка: **test_get_book_genre_book_not_exists_negative**
* Получение списка книг определенного жанра: **test_get_book_with_specific_genre**
* Получение списка книг жанра не из списка: **test_get_book_with_specific_genre_not_exists_negative**
* Смена жанра книги: **test_change_book_genre**
* Смена жанра книги на несуществующий: **test_change_book_genre_to_not_exists_negative**
* Получение книг без возрастного рейтинга: **test_get_books_for_children**
* Добавление книг в избранное: **test_add_book_in_favorites**
* Добавление в избранное книги не из списка книг: **test_add_book_in_favorites_book_not_exists_negative**
* Удаление книги из избранного: **test_remove_book_from_favorites**
* Получение списка избранного: **test_get_list_favorites**

**Тестовое покрытие составляет 97%**