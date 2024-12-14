#!/usr/bin/env python3

import random
import sys

def main():
    try:
        A = random.randint(-10, 10)
        print(A)
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"A: {A}\n")
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()