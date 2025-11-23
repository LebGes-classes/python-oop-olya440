from Book import (
    Book,
)
from Menu import (
    Menu,
)


menu = Menu()
book_1 = Book()
book_2 = Book("1984", "Джордж Оруэл", 320)


def run() -> None:
    """Метод запуска работы."""

    is_running = True

    while (is_running):
        menu.print_main_menu()

        choise = int(input('Введите выбор: '))
        choise_book = int(input('Введите порядковый номер книги: '))
        book = book_1 if choise_book == 1 else book_2

        is_running = menu.main_menu(choise, book)


run()