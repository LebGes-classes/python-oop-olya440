class Book:
    def __init__(self, title="", author="", pages=1):
        # Используем сеттеры для проверки
        self.set_title(title)
        self.set_author(author)
        self.set_pages(pages)

    def set_title(self, title):
        self._title = str(title)

    def get_title(self):
        return self._title

    def set_author(self, author):
        self._author = str(author)

    def get_author(self):
        return self._author

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("Страницы должны быть положительным целым числом.")

    def get_pages(self):
        return self._pages

    def display(self):
        print(f"Название: {self._title}, Автор: {self._author}, Страниц: {self._pages}")

    # Два дополнительных метода
    def is_long(self):
        return self._pages > 300

    def compare_pages(self, other):
        if not isinstance(other, Book):
            return "Сравнение возможно только с объектом Book."
        diff = self._pages - other.get_pages()
        if diff > 0:
            return f"'{self._title}' длиннее на {diff} стр."
        elif diff < 0:
            return f"'{self._title}' короче на {-diff} стр."
        return f"'{self._title}' и '{other.get_title()}' одинаковой длины."


class Main:
    @staticmethod
    def run():
        # Создание двух экземпляров
        book1 = Book("1984", "Оруэлл", 328)
        book2 = Book()  # без параметров

        print("Демонстрация:")
        book1.display()
        print(f"Книга '{book1.get_title()}' длинная? {book1.is_long()}")

        print("\n--- Интерактивное меню ---")
        Main.run_menu()

    @staticmethod
    def run_menu():
        books = []
        while True:
            print("\n1. Создать книгу (с параметрами)")
            print("2. Создать книгу (по умолчанию)")
            print("3. Просмотреть все книги")
            print("4. Сравнить две книги")
            print("0. Выйти")
            choice = input("Выберите: ")

            if choice == '0':
                break
            elif choice == '1':
                try:
                    t = input("Название: ")
                    a = input("Автор: ")
                    p = int(input("Страницы: "))
                    books.append(Book(t, a, p))
                    print("Книга создана.")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            elif choice == '2':
                books.append(Book("Новая Книга", "Неизвестный", 100))
                print("Книга по умолчанию создана.")
            elif choice == '3':
                for i, b in enumerate(books):
                    print(f"{i+1}. ", end=""); b.display()
            elif choice == '4':
                if len(books) < 2:
                    print("Нужно минимум 2 книги.")
                    continue
                try:
                    idx1 = int(input("Номер 1-й книги: ")) - 1
                    idx2 = int(input("Номер 2-й книги: ")) - 1
                    print(books[idx1].compare_pages(books[idx2]))
                except (ValueError, IndexError):
                    print("Неверный номер.")
            else:
                print("Неверный выбор.")



Main.run()
