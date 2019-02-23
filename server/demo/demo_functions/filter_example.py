from demo.demo_functions.random_data import random_integers


def search_for_number():
    found = []
    for integer in random_integers:
        if integer % 42 == 0:
            found.append(integer)
    return found
