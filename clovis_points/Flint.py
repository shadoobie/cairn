from random import random

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
    learning_rate = 0
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

    def train_2_inputs_1_output_(self, iterations, input1, input2):
        for i in range(iterations):
            self.calculate_error(input1, input2, )
