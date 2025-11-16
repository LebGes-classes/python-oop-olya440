class Book:
    def __init__(self, title='Без названия', author='Неизвестен', pages=1):
        # Конструктор с параметрами, с значениями по умолчанию
        self.__title = title
        self.__author = author
        self.__pages = pages
        # Проверка корректности при создании
        if pages <= 0:
            print('Количество страниц должно быть положительным. Установлено значение 1.')
            self.__pages = 1

    # Методы get для доступа к приватным полям
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    # Методы set для изменения приватных полей с проверкой
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_pages(self, pages):
        if pages <= 0:
            print('Количество страниц должно быть положительным.')
            # Не меняем значение, если оно некорректное
        else:
            self.__pages = pages

    # Метод для просмотра информации
    def show_info(self):
        print(f'Название: {self.__title}, Автор: {self.__author}, Страниц: {self.__pages}')

    # Собственные методы
    def is_long(self):
        """Проверяет, является ли книга длинной."""
        return self.__long > 300

    def reset(self):
        """Сбрасывает атрибуты книги к значениям по умолчанию."""
        self.__title = 'Без названия'
        self.__author = 'Неизвестен'
        self.__pages = 1


class Menu:
    def __init__(self, book: Book):
        self.book = book

    def show_menu(self):
        print("\n--- МЕНЮ ---")
        print("1. Показать информацию")
        print("2. Изменить название")
        print("3. Изменить автора")
        print("4. Изменить количество страниц")
        print("5. Это длинная книга? (страниц > 300)")
        print("6. Сбросить данные")
        print("EXIT - выход")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ").strip()

            if choice == '1':
                self.book.show_info()
            elif choice == '2':
                new_title = input("Введите новое название: ")
                self.book.set_title(new_title)
            elif choice == '3':
                new_author = input("Введите нового автора: ")
                self.book.set_author(new_author)
            elif choice == '4':
                try:
                    new_pages = int(input("Введите количество страниц (>0): "))
                    self.book.set_pages(new_pages) # Проверка внутри метода set_pages
                except ValueError:
                    print("Пожалуйста, введите целое число.")
            elif choice == '5':
                if self.book.is_long():
                    print("Да, это длинная книга.")
                else:
                    print("Нет, это не длинная книга.")
            elif choice == '6':
                self.book.reset()
                print("Данные книги сброшены.")
            elif choice.upper() == 'EXIT':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


class Main:
    # Создание двух экземпляров класса Book
    book1 = Book()  # вызывается конструктор без параметров (с дефолтными значениями)
    book2 = Book("1984", "Джордж Оруэлл", 328)  # вызывается конструктор с параметрами

    print("Создано 2 книги:")
    book1.show_info()
    book2.show_info()

    # Выбор книги для взаимодействия
    book_choice = input("\nВыберите книгу (1 или 2): ").strip()
    selected_book = None

    if book_choice == '1':
        selected_book = book1
    elif book_choice == '2':
        selected_book = book2
    else:
        print("Неверный выбор. Завершение.")
        exit()

    # Создание и запуск меню для выбранной книги
    menu = Menu(selected_book)
    menu.run()
