#!/usr/bin/env python3

import math
import sys


def main():
    try:
        C = float(sys.stdin.read().strip())
        sqrt_C = math.sqrt(C)
        with open("output.txt", "w") as output_file:
            output_file.write(f"Sqrt: {sqrt_C}\n")
        with open("logs.txt", "a") as log_file:
            log_file.write(f"C: {C}, sqrt(C): {sqrt_C}\n")
    except ValueError as ve:
        sys.stderr.write(f"Error: {str(ve)}\n")
    except Exception as ex:
        sys.stderr.write(f"Error: {str(ex)}\n")


if __name__ == "__main__":
    main()
