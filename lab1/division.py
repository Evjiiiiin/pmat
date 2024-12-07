#!/usr/bin/env python3

import random
import sys

def get_integer_input():
    while True:
        try:
            return int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка: введите корректное целое число.")

def main():
    A = get_integer_input()
    B = random.randint(-10, 10)

    if B == 0:
        sys.stderr.write("Ошибка: деление на ноль.\n")
        return

    result = A / B
    print(f"Результат деления: {result}")

if __name__ == "__main__":
    main()
