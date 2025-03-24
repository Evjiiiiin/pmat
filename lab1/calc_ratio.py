#!/usr/bin/env python3

import random
import sys


def main():
    try:
        A = int(sys.stdin.read().strip())
        B = random.randint(-10, 10)
        ratio = A / B
        print(ratio)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"B: {B}, A/B: {ratio}\n")
    except ZeroDivisionError:
        sys.stderr.write("Error: Division by zero.\n")
    except ValueError as ve:
        sys.stderr.write(f"Error: {str(ve)}\n")
    except Exception as ex:
        sys.stderr.write(f"Error: {str(ex)}\n")


if __name__ == "__main__":
    main()
