# Exercises without loops

import math

# 1.1
# Write the famous Hello World! program in Python.


def ex1_1():
    print("Hello World!")


# 1.2
# Write a program that asks the user for their name and then greets them using that name.
# Use the print and input commands.

def ex1_2():
    print("The greeting program v. 1.0")
    name = input("Enter your name: ")
    print(f"Hi {name}!")


# 1.3
# Write a program that solves a given quadratic equation.
# Make sure that your code properly handles all cases (but assume that the user enters - when asked - integers).


def solve_linear(b, c):
    if b == 0:
        if c == 0:
            print("The equation has infinitely many solutions")
        else:
            print("The equation has no solutions")
    else:
        x = -c / b
        print(f"The equation has one real root: {x}")


def ex1_3():
    print("The quadratic equation solver v. 1.0")
    a = int(input("Enter the quadratic coefficient: "))
    b = int(input("Enter the linear coefficient: "))
    c = int(input("Enter the free term: "))
    if a == 0:
        solve_linear(b, c)
        return

    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"The equation has two real roots: {x1:.2f} and {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"The equation has one real root: {x:.2f}")
    else:
        print("The equation has no real roots")
        real = -b / (2 * a)
        imag = math.sqrt(-delta) / (2 * a)
        print(f"The complex roots are: {real:.2f} + {imag:.2f}i and {real:.2f} - {imag:.2f}i")

# ex1_4
# Write a program collecting details of a pizza order. Assume (in your code) some set of sauces, toppings, and their prices. After collecting all data display a description of the pizza and its price. You can assume that the client, though hungry, always gives valid answers.

def ex1_4():
    print("Pizzarino Ltd. The best pizza deliveries in this century and galaxy!")
    order = "You have ordered a pizza with: "
    price = 0
    sauce = input("Do you want the (T)omato or (M)ayonnaise sauce? ")
    if sauce == "T":
        order += "tomato sauce, "
        price += 2
    elif sauce == "M":
        order += "mayonnaise sauce, "
        price += 3

    onion = input("Do you want onion (Y/N)? ")
    if onion == "Y":
        order += "onion, "
        price += 1

    mushrooms = input("Do you want mushrooms (Y/N)? ")
    if mushrooms == "Y":
        order += "mushrooms, "
        price += 2

    jalapenos = input("Do you want jalapenos (Y/N)? ")
    if jalapenos == "Y":
        order += "jalapenos, "
        price += 3

    corn = input("Do you want corn (Y/N)? ")
    if corn == "Y":
        order += "corn, "
        price += 2

    black_olives = input("Do you want black olive (Y/N)? ")
    if black_olives == "Y":
        order += "black olives, "
        price += 2

    print(order, "The price is: ", price, "$. Enjoy your meal!")


if __name__ == "__main__":
    # ex1_1()
    # ex1_2()
    # ex1_3()
    ex1_4()
