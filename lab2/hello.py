#!/usr/bin/python3
import string

def is_valid_name(name):
    return name[0].isupper() and name[1:].islower() and all(c in string.ascii_letters for c in name)

def greet_user():
    while True:
        try:
            name = input().strip()
            if is_valid_name(name):
                print(f"Привет, {name}!")
            else:
                print(f"Неверное имя: {name}. Оно должно начинаться с заглавной буквы и содержать только буквы.")
        except KeyboardInterrupt:
            print("\nДо свидания!")
            break

def greet_names_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for name in file:
                name = name.strip()
                if is_valid_name(name):
                    print(f"Привет, {name}!")
                else:
                    print(f"Неверное имя: {name}. Оно должно начинаться с заглавной буквы и содержать только буквы.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    choice = input().strip()
    
    def switch(case):
        return {
            '1': greet_user,
            '2': lambda: greet_names_from_file('name.txt')
        }.get(case, lambda: print("Неверный выбор. Пожалуйста, выберите 1 или 2."))()

    switch(choice)

if __name__ == "__main__":
    main()
