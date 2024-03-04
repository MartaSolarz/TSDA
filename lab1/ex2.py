# Exercises with loops

import sys
import random
import math

# 1.1
# Write a program that prints out all its command-line parameters,
# each prefixed with a number representing its position.


def ex1_1():
    print("List of command-line arguments")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i}: {arg}")

# 1.2
# Write a program that takes an integer and displays its factorization into prime numbers.
# Assume that the user enters a valid integer number.


def ex1_2():
    print("Factorizer Pro (TM)")
    entry_num = int(input("Enter the number for factorization: "))
    n = entry_num
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(str(i))
            n //= i
        i += 1

    result = "*".join(factors)

    print(f"{entry_num} = {result}")

# 1.3
# Write a program that calculates an approximation of the pi number using the Monte-Carlo method.
# The program should ask the user for the total number of iterations and the step of printing
# and then display the current approximation after each step number of iterations and then the final value.


def ex1_3():
    print("Monte-Carlo pi approximator.")
    total = int(input("Enter the total number of iterations: "))
    step = int(input("Enter the display step: "))
    inside = 0
    for i in range(1, total + 1):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
        if i % step == 0:
            print(f"{i}: {4 * inside / i}")

    print(f"The calculated final value is: {4 * inside / total}")
    print(f"Python math.pi equals: {math.pi}")


if __name__ == "__main__":
    ex1_2()
