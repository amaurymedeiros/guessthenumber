from random import shuffle

def get_random_number():
    numbers = list('1234567890')
    shuffle(numbers)
    return int(''.join(numbers[:4]))

def calculate_score(secret, guess):
    black_pins = 0
    white_pins = 0
    for index, digit in enumerate('%04d' % guess):
        try:
            secret_index = ('%04d' % secret).index(digit)
        except ValueError:
            continue
        if index == secret_index:
            black_pins += 1
        else:
            white_pins += 1
    return {'black_pins' : black_pins, 'white_pins' : white_pins}