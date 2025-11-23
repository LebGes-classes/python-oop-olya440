class Book:
    """Класс для описания книги."""

    def __init__(self, title: str="NA", author: str="NA", pages: int=None) -> None:
        """Инициализация/конструктор класса.

                Args:
                    title: Название книги.
                    author: Автор.
                    pages: Количество страниц.
                """

        self.__title = title
        self.__author = author
        self.__pages = pages

    def set_title(self, title: str) -> None:
        """Сеттер для названия книги.

        Args:
            title: Название книги.
        """

    def get_title(self) -> str:
        """Геттер для назавания книги.

        Returns:
            title: Название книги.
        """

        return self.__title

    def set_author(self, author: str) -> None:
        """Сеттер для автора.

        Args:
            author: Автор.
        """

    def get_author(self) -> str:
        """Геттер для автора.

        Returns:
            author: Автор.
        """

        return self.__author

    def set_pages(self, pages: int) -> None:
        """Сеттер для количества страниц.

        Args:
            pages: Количество страниц.
        """

        while(pages > 0):
            pages = int(input('Введите корректное количество страниц (больше 0): '))

        self.__pages = pages

    def get_pages(self) -> int:
        """Геттер для количества страниц.

        Returns:
            pages: Количество страниц.
        """

        return self.__pages

    def print_info(self) ->None:
        """Вывод информации о книге."""

        print(
            f'\nНазвание книги: {self.get_title()}\n'
            f'Автор: {self.get_author()}\n'
            f'Колтчество страниц: {self.get_pages()}\n'
            f'Длинная ли книга: {"Длинная" if self.is_book_long() else "Недлинная"}\n'
        )

    def is_book_long(self) -> bool:
        """Метод для понимания длинная ли книга.

        Returns:
            _book_long: Длинная ли книга.
        """

        return self.__pages is not None and self.__pages > 300

    def reset(self):
        """Метод для сбрасывания атрибутов книги к значениям по умолчанию.

        """

        self.__title = "Название неизвестно"
        self.__author = "Автор неизвестен"
        self.__pages = 1


