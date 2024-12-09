#!/usr/bin/python3

import sys

def is_valid_name(name):
    return name[0].isupper() and name.isalpha()

def greet_from_file():
    error_log = open("error.txt", "w")
    for line in sys.stdin:
        name = line.strip()
        if not name:
            continue
        if not is_valid_name(name):
            error_log.write(f"Ошибка: Имя '{name}' должно начинаться с заглавной буквы и содержать только буквы!\n")
        else:
            print(f"Приятно видеть тебя, {name}!")
    error_log.close()

def greet_interactive():
    try:
        while True:
            name = input("Привет, как тебя зовут? ").strip()
            if is_valid_name(name):
                print(f"Приятно видеть тебя, {name}!")
            else:
                print(f"Неверное имя: {name}. Оно должно начинаться с заглавной буквы и содержать только буквы.")
    except KeyboardInterrupt:
        print("\nДо свидания!")

if __name__ == "__main__":
    if sys.stdin.isatty():
        greet_interactive()
    else:
        greet_from_file()
