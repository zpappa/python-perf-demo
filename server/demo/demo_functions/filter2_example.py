from demo.demo_functions.random_data import random_integers


def search_for_number():
    return list(filter(lambda x: x % 42 == 0, random_integers))
