"""
Additional Task (not obligatory, possibility to get additional points)

A long time ago in a galaxy (not so) far, far away... we have 1000 bottles and 10 brave adventurers.
The task is to detect 1 special bottle hidden among those 1000.
All bottles contain water, and are indistinguishable, as the water inside them is too.
Everyone who will drink from the special bottle will lose the ability to speak for a year, but the effect starts the next day.
The water in bottles never ends (or can be divided infinitely), so everyone is able to drink from every bottle.
The effect of the special bottle is inevitable, no matter if somebody drinks only one drop or more from it.
Design a system of detecting the special bottle in one day, that minimizes the number of people affected.

HINT: Effect of special bottle starts the next day, that means you have only one iteration.

(A) What is the maximal number of people affected (in worst case scenario)?

HINT: If you invent a system, the answer need no computation.
(B) Show the sample simulation as follows:
    Special bottle number is 123

    Person 1 will drink from bottles 1,2,3,...,100
    Person 2 will drink from bottles...
    ...
    Person 10 will drink from bottles ...

    Total number of brave adventurers that will drink from special bottle is ...
"""

special_bottle = 123

# divide and win strategy
# we will use binary representation of the bottle number
# each person will drink from bottles with 1 at the corresponding position
# if the special bottle has 1 at the position, the person will drink from it
# if it has 0, the person will not drink from it
# this way we can detect the special bottle in one iteration
# the maximum number of people affected is 10
def simulate_special_bottle(special_bottle):
    special_bottle_binary = format(special_bottle, '010b')

    result = []
    for i in range(10):
        person_drinks_from = []
        for bottle in range(1, 1001):
            if format(bottle, '010b')[i] == '1':
                person_drinks_from.append(bottle)

        will_drink_from_special = 'will' if special_bottle_binary[i] == '1' else 'will not'
        result.append(f"Person {i + 1} {will_drink_from_special} drink from the special bottle.")

    affected = sum([1 for bit in special_bottle_binary if bit == '1'])

    return result, affected


if __name__ == "__main__":
    simulation_result, total_affected = simulate_special_bottle(special_bottle)
    for line in simulation_result:
        print(line)
    print(f"Total number of brave adventurers that will drink from special bottle is {total_affected}.")
