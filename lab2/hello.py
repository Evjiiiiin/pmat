#!/usr/bin/python3
import string

def is_valid_name(name):
    return name[0].isupper() and name[1:].islower() and all(c in string.ascii_letters for c in name)

def greet_user():
    try:
        while True:
            name = input("Пожалуйста, введите ваше имя: ").strip()
            if is_valid_name(name):
                print(f"Привет, {name}!")
            else:
                print(f"Неверное имя: {name}. Оно должно начинаться с заглавной буквы и содержать только буквы.")
    except KeyboardInterrupt:
        print("\nДо свидания!")

def greet_names_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            names = file.readlines()
            for name in names:
                name = name.strip()  # Удаляем пробелы и символы новой строки
                if is_valid_name(name):
                    print(f"Привет, {name}!")
                else:
                    print(f"Неверное имя: {name}. Оно должно начинаться с заглавной буквы и содержать только буквы.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    choice = input("Выберите 1 для приветствия или 2 для чтения имен из файла: ").strip()
    if choice == '1':
        greet_user()
    elif choice == '2':
        greet_names_from_file('name.txt')
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
