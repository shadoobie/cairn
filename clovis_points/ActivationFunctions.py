import numpy


class ActivationFunctions:

    @staticmethod
    def sigmoid_function(input1, input2, bias, weights):
        # Sigmoid Function
        outp_pn = input1 * weights[0] + \
                  input2 * weights[1] + \
                  bias * weights[2]
        return 1.0 / (1 + numpy.exp(-outp_pn))
