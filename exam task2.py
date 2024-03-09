import random

def get_random(number=3):
    if not isinstance(number, int) or number < 1:
        raise Exception('Invalid data!')

    drawn_numbers = set()
    while len(drawn_numbers) < number:
        drawn_numbers.add(random.randint(1, 100))

    return sorted(list(drawn_numbers))

print(get_random())
