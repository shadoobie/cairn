def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


class GeneratorFunctions:

    def __init__(self):
        print('no this is printed first.')

    # A simple generator function

