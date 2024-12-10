#!/usr/bin/env python3

import random
import sys

def get_integer_input():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Ошибка: введите корректное целое число.")

def main():
    A = get_integer_input()
    B = random.randint(-10, 10)

    try:
        result = A / B
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        with open("error.txt", "a") as error_log:
            error_log.write("Ошибка: деление на ноль.\n")

if __name__ == "__main__":
    main()
