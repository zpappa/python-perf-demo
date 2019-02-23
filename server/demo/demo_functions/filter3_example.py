from demo.demo_functions.random_data import random_integers

def search_for_number():
    return list(filter(None, [x if x % 42 == 0 else None for x in random_integers]))
