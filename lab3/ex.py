# Exercises with data structures

# Exercise 1
# Design a data structure for a phone book with your friends' phone numbers.
# Assume that your friends only have one first name and that no two friends have the same both first name and surname.
# Make sure that your data structure allows for keeping several (any number) phone numbers per friend.
# Accept phone numbers of any structure
# (e.g. different lengths, which may be due - among others - to having or skipping the country code).
# Assume for now that the phone numbers are not marked with any labels.

# Implement the following operations:

# creating an empty phone book,
# inserting a new number for a given person,
# retrieving (any) number of the indicated person,
# deleting the given number of the given person and
# printing the entire book.
# Also, write a program testing your solution for several people and telephone numbers.
# Make sure that each operation is executed at least once.

# Sample printout of the phone book:

# Ala Wesołowska: +048 513 056 121, 22-848-34-21
# John Smith: 469-452-199, 0800 241 6331
# Susan Brown: 315-728-3639


import dataclasses


@dataclasses.dataclass
class PhoneBook:
    phone_book: {}

    def insert(self, name, number):
        if name not in self.phone_book:
            self.phone_book[name] = []
        self.phone_book[name].append(number)

    def retrieve(self, name):
        return self.phone_book[name]

    def delete(self, name, number):
        self.phone_book[name].remove(number)

    def print(self):
        for name, numbers in self.phone_book.items():
            print(f"{name}: {', '.join(numbers)}")


# phone_book = PhoneBook({})
# phone_book.insert("Ala Wesołowska", "+048 513 056 121")
# phone_book.insert("Ala Wesołowska", "22-848-34-21")
# phone_book.insert("John Smith", "469-452-199")
# phone_book.insert("John Smith", "0800 241 6331")
# phone_book.insert("Susan Brown", "315-728-3639")
# phone_book.print()
# print('----------------')
# phone_book.delete("Ala Wesołowska", "22-848-34-21")
# phone_book.print()
# print('----------------')
# number = phone_book.retrieve("John Smith")
# print(number)

# Exercise 2
# Consider the following modifications to the previous exercise.

# a) Try to use in the solution of the previous exercise different ways of remembering the name and surname:

# a string (space separated), --> ok
# a tuple (pair), --> ok
# a two-element list. --> unhashable type: 'list'
# Discuss these solutions (are they all applicable?).

# b) Allow for labeling of the phone numbers (e.g. home, main, work, etc.). How it influences your data structure?

# add label to the insert method, print method and delete method

# c) Does your structure allow you to insert the same phone number several times for one person?
# What to do to prevent this from happening?

# add check if number is already in the list

# d) Does your structure allow to insert the same phone number several times (maybe for different people)?
# What to do to prevent this from happening?

# add check if number is already in the list

# Sample printout of the phone book may look as follows:

# Ala Wesołowska: main: + 048 513 056 142, + 048 798-123-422;
# John Smith: main: 0 800 241 6331; work: 469 - 452 - 199;
# Susan Brown: work: 315 - 728 - 3639;


@dataclasses.dataclass
class PhoneBookV2:
    phone_book: {}

    def insert(self, name, number, label):
        if type(name) == list:
            name = ' '.join(name)
        if name not in self.phone_book:
            self.phone_book[name] = {}
        if label not in self.phone_book[name]:
            self.phone_book[name][label] = []
        if number not in self.phone_book[name][label]:  # if we don't want to allow the same number for the same person
            self.phone_book[name][label].append(number)

        # self.phone_book[name][label].append(number) # if we want to allow the same number for the same person

        # if we don't want to allow the same number for different people
        # for person, numbers in self.phone_book.items():
        #     for label, number in numbers.items():
        #         if number == number:
        #             print("Number already exists in the phone book!")
        #             return
        #
        # self.phone_book[name][label].append(number)


    def retrieve(self, name):
        return self.phone_book[name]

    def delete(self, name, number, label):
        self.phone_book[name][label].remove(number)

    def print(self):
        for name, numbers in self.phone_book.items():
            print("%s: %s" % (name, ", ".join([f"{label}: {', '.join(numbers)}" for label, numbers in numbers.items()])))


phone_book = PhoneBookV2({})
# A - name as a string (space separated)
phone_book.insert("Ala, Wesołowska", "+048 513 056 121", "main")
# B - name as a tuple (pair)
phone_book.insert(("Ala", "Wesołowska"), "+048 798-123-422", "main")
# C - name as a two-element list
phone_book.insert(["John", "Smith"], "0 800 241 6331", "main")
phone_book.insert("John Smith", "469 - 452 - 199", "work")
phone_book.insert("Susan Brown", "315 - 728 - 3639", "work")
phone_book.print()
print('----------------')
phone_book.delete(("Ala", "Wesołowska"), "+048 798-123-422", "main")
phone_book.print()
print('----------------')
number = phone_book.retrieve("John Smith")
print(number)

# Exercise 3
# Write the Eratosthenes Sieve algorithm that prints out all the prime numbers not greater than
# the given as parameter value.
# What data structure will you use?

# The algorithm for the given value n works as follows.
# First, all numbers from 2 up to n are written out (e.g. on a piece of paper) one by one.
# Then we proceed (starting from 2) from the smallest numbers up analyzing each number in turn.
# If the given number is not crossed out, then we cross out all of its multiplications.
# If the number is already crossed out we do nothing with it. In both cases, we proceed to the next number.
# The algorithm stops when we reach and analyze the last number (n).
# All numbers which are not crossed out after the execution of this algorithm are prime numbers
# (and all the prime numbers) from the range 2..n.

# Try to justify the correctness of this algorithm.

# Sample output:

# primes up to 11: [2, 3, 5, 7, 11]


def eratosthenes_sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


print(eratosthenes_sieve(11))

# Exercise 4
# Write a function pos(word, text) for finding the left-most appearance of a non-empty string word
# within a string 'text' at every second character.
# If such occurrence exists then the function should return the index within text of the first character
# of the found appearance otherwise, the function should return -1.

# Try to use slices. What is the complexity of this algorithm?

# Sample results of the function:

# pos("a", "") == -1
# pos("hsal", "Mary has a little lamb") == 5


def pos(word, text):
    for i in range(1, len(text), 2):
        if text[i:i + len(word)] == word:
            return i
    return -1


print(pos("a", ""))
print(pos("has", "Mary has a little lamb"))

# Exercise 5
# Write a function sublist(lst1, lst2) that checks if the first given list appears in the second.
# Note: The items from lst1 do not have to appear next to each other in the lst2 list,
# but their order must be preserved.

# Sample results of the function:

# sublist([], []) == True
# sublist([], [1, 2, 3]) = True
# sublist([2], [1, 2, 3]) == True
# sublist([1, 3, 4], [1, 2, 3, 4, 5]) == True
# sublist([1, 4, 3], [1, 2, 3, 4, 5]) == False


# def sublist(lst1, lst2):
#     it = iter(lst2)  # Create an iterator over lst2
#     return all(item in it for item in lst1)

def sublist(lst1, lst2):
    lst2_index = 0
    for item1 in lst1:
        found = False
        for i in range(lst2_index, len(lst2)):
            if lst2[i] == item1:
                lst2_index = i + 1
                found = True
                break
        if not found:
            return False
    return True


print(sublist([], []))
print(sublist([], [1, 2, 3]))
print(sublist([2], [1, 2, 3]))
print(sublist([1, 3, 4], [1, 2, 3, 4, 5]))
print(sublist([1, 4, 3], [1, 2, 3, 4, 5]))

# Exercise 6 [extension]
# Suggest a data structure to represent the checkers game board
# (stones are of two colors, they stand only on black squares, some are queens).
# Write a function that generates all possible moves for the player playing stones of the color
# given by the function parameter.

# What data structure will you use to represent the board and the result?

board = [
    [None, ('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal')],
    [('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal'), None],
    [None, ('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal'), None, ('black', 'normal')],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal'), None],
    [None, ('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal')],
    [('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal'), None, ('white', 'normal'), None]
]

def generate_moves(board, color):
    moves = []
    directions = [(-1, -1), (-1, 1)] if color == 'black' else [(1, -1), (1, 1)]
    for i in range(8):
        for j in range(8):
            if board[i][j] is not None and board[i][j][0] == color:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < 8 and 0 <= nj < 8 and board[ni][nj] is None:
                        moves.append(((i, j), (ni, nj)))
    return moves

# Example usage
color = 'black'  # or 'white'
possible_moves = generate_moves(board, color)
print(possible_moves)


name = {
    ("name", "surname"): "value"
}

print(name[("name", "surname")])  # value

