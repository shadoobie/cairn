from random import random

import numpy

from clovis_points import ActivationFunctions


def __init_truth_table__(operation):
    table = []
    if operation in ['or', 'OR', '|']:
        table.append([0, 0, 0])
        table.append([1, 1, 1])
        table.append([1, 0, 1])
        table.append([0, 1, 1])
    elif operation in ['and', 'AND', '&']:
        table.append([0, 0, 0])
        table.append([1, 1, 1])
        table.append([1, 0, 0])
        table.append([0, 1, 0])

    return table


class Flint:
    learning_rate = 0 #(Lithic reduction)
    bias = 0
    weights = None
    truth_table = None

    def __init__(self, learning_rate, bias, operation):
        self.learning_rate = learning_rate
        self.bias = bias
        self.truth_table = __init_truth_table__(operation)
        self.weights = list()
        for k in range(3):
            self.weights.append(random.random())  # Assigning random weights

    def calculate_error(self, input1, input2, expected_output):
        sigmoid_output = ActivationFunctions.sigmoid_function(input1,
                                                              input2,
                                                              self.bias,
                                                              self.weights)
        error = expected_output - sigmoid_output
        return error

    def modify_weights_training(self, error, input1, input2):
        self.weights[0] += error * input1 * self.learning_rate
        self.weights[1] += error * input2 * self.learning_rate
        self.weights[2] += error * self.bias * self.learning_rate

    def train_2_inputs_1_output_(self, iterations):
        for i in range(iterations):
            error = self.calculate_error(self.truth_table[0],
                                         self.truth_table[1],
                                         self.truth_table[2])
            self.modify_weights_training(error,
                                         self.truth_table[0],
                                         self.truth_table[1])

        for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            outp_pn = x * self.weights[0] + y * self.weights[1] + self.bias * self.weights[2]
            # Based on the trained wieghts
            outp = 1.0 / (1 + numpy.exp(-outp_pn))
            print(str(x) + " AND " + str(y) + " yields: " + str(outp))
