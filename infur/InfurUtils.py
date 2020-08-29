class InfurUtils:

    def from_wei(self, wei_number):
        return self.move_decimal_point(wei_number, 18)

    '''
        credit: m3trik on https://stackoverflow.com/questions/8362792/how-do-i-shift-the-decimal-place-in-python/8362821
        Move the decimal place in a given number.

        args:
            num (int)(float) = The number in which you are modifying.
            decimal_places (int) = The number of decimal places to move.

        returns:
            (float)

        ex. moveDecimalPoint(11.05, -2) returns: 0.1105
        '''
    def move_decimal_point(self, num, decimal_places):
        for _ in range(abs(decimal_places)):

            if decimal_places > 0:
                num *= 10;  # shifts decimal place right
            else:
                num /= 10.;  # shifts decimal place left

        return float(num)