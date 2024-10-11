#!/usr/bin/env python3

import random

a = int(input("Enter a number: "))
print (f"A = {a}")

b = random.randint(-10, 10)
print(f"B = {b}")

try:
	result = a /b
	print(f"A/B = {result}")
except ZeroDivisionError:
	print("Error: Division by zero is not allowed")
