from Book import (
    Book,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def print_main_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\n1: Печать информации о книге.\n'
            '2: Изменить название книги.\n'
            '3: Изменить автора.\n'
            '4: Изменить количество страниц.\n'
            '5: Получить информацию о названии книги.\n'
            '6: Получить информацию о названии книги.\n'
            '7: Получить информацию о количестве страниц.\n'
            '8: Получить информацию о том, длинная ли книга.\n'
            '9: Сбросить все атрибуты книги.\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ!\n'
        )

    def main_menu(self, choise: int, book: Book) -> bool:
        """Главное пользовательское меню.

        Args:
            choise: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choise:
            case 0:
                is_running = False
            case 1:
                book.print_info()
            case 2:
                title = input('Введите название книги: ')

                book.set_title(title)
            case 3:
                author = input('Введите автора: ')

                book.set_author(author)
            case 4:
                pages = int(input('Введите корректное количество страниц (больше 0): '))

                book.set_pages(pages)
            case 5:
                print(book.get_title())
            case 6:
                print(book.get_author())
            case 7:
                print(book.get_pages())
            case 8:
                print(f'Книга длинная?: {"Длинная." if book.is_book_long() else "Недлинная."}')
            case 9:
                print(book.reset())

        return is_running