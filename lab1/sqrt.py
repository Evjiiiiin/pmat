#!/usr/bin/env python3

import sys
import math

def main():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        
        if number < 0:
            raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа.")
        
        result = math.sqrt(number)
        
        with open('output.txt', 'w') as file:
            file.write(f"{result}\n")
    
    except ValueError as ve:
        sys.stderr.write(f"Ошибка: {str(ve)}\n")
    except Exception as ex:
        sys.stderr.write(f"Ошибка: {str(ex)}\n")

if __name__ == "__main__":
    main()
