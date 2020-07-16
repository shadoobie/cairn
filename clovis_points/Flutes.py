class Flutes:
    error = None
    actual = None

    def __init__(self, error, actual):
        self.error = error
        self.actual = actual

    def get_error(self):
        return self.error

    def get_actual(self):
        return self.actual