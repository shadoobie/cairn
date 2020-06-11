from random import random

import numpy

from clovis_points import ActivationFunctions
from clovis_points import TruthTables as tt


class Flint:
    learning_rate = 0  # (Lithic reduction)
    bias = 0
    weights = None
    truth_table = None

    def __init__(self, learning_rate, bias, operation):
        self.learning_rate = learning_rate
        self.bias = bias
        self.truth_table = self.determine_truth_table(operation)
        self.weights = list()
        for k in range(3):
            self.weights.append(random.random())  # Assigning random weights

    def determine_truth_table(self, operation):
        if operation in ['and', 'AND', '&']:
            return tt.TruthTables.and_truth_table()
        elif operation in ['or', 'OR', '|']:
            return tt.TruthTables.or_truth_table()

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
            # Based on the trained weights
            outp = 1.0 / (1 + numpy.exp(-outp_pn))
            print(str(x) + " AND " + str(y) + " yields: " + str(outp))
