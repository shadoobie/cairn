from random import random

import numpy
import random

from clovis_points import ActivationFunctions as af
from clovis_points import TruthTables as tt


class Flint:
    learning_rate = 0  # (Lithic reduction)
    bias = 0
    weights = None
    truth_table = None
    operation = None

    def __init__(self, learning_rate, bias, operation):
        self.learning_rate = learning_rate
        self.bias = bias
        self.truth_table = self.__determine_truth_table__(operation)
        self.weights = list()
        for k in range(3):
            self.weights.append(random.random())  # Assigning random weights

    def __determine_truth_table__(self, operation):
        if operation in ['and', 'AND', 'And', '&']:
            self.operation = 'AND'
            return tt.TruthTables.and_truth_table()
        elif operation in ['or', 'OR', 'Or', '|']:
            self.operation = 'OR'
            return tt.TruthTables.or_truth_table()
        elif operation in ['not', 'NOT', 'Not', '-']:
            self.operation = 'NOT'
            return tt.TruthTables.not_truth_table()

    def calculate_error(self, input1, input2, expected_output):
        actual_output = af.ActivationFunctions.sigmoid_function(input1,
                                                                 input2,
                                                                 self.bias,
                                                                 self.weights)
        error = expected_output - actual_output
        return error

    def calculate_error_for_not(self, input1, expected_output):
        sigmoid_output = af.ActivationFunctions.sigmoid_function_single_input(input1,
                                                                 self.bias,
                                                                 self.weights)
        error = expected_output - sigmoid_output
        return error

    def modify_weights_training(self, error, input1, input2):
        self.weights[0] += error * input1 * self.learning_rate
        self.weights[1] += error * input2 * self.learning_rate
        self.weights[2] += error * self.bias * self.learning_rate

    def calcualte_error_and_modify_weights_for_case(self, case):
        error = self.calculate_error(self.truth_table[case].get('input1'),
                                     self.truth_table[case].get('input2'),
                                     self.truth_table[case].get('expected_output'))
        self.modify_weights_training(error,
                                     self.truth_table[case].get('input1'),
                                     self.truth_table[case].get('input2'))

    def calcualte_error_and_modify_weights_for_not(self, case):
        error = self.calculate_error_for_not(self.truth_table[case].get('input1'),
                                     self.truth_table[case].get('expected_output'))
        self.modify_weights_training_for_not(error,
                                     self.truth_table[case].get('input1'))

    def modify_weights_training_for_not(self, error, input1):
        self.weights[0] += error * input1 * self.learning_rate
        self.weights[2] += error * self.bias * self.learning_rate

    def train_2_inputs_1_output(self, iterations):
        for i in range(iterations):
            for n in range(4):
                case = 'case' + str(n+1)
                self.calcualte_error_and_modify_weights_for_case(case)

        for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            outp_pn = x * self.weights[0] + y * self.weights[1] + self.bias * self.weights[2]
            # Based on the trained weights
            outp = 1.0 / (1 + numpy.exp(-outp_pn))
            print(str(x) + " " + self.operation + " " + str(y) + " yields: " + str(outp))

    def train_1_input_to_1_output(self, iterations):
        for i in range(iterations):
            for n in range(2):
                case = 'case' + str(n+1)
                self.calcualte_error_and_modify_weights_for_not(case)

        for x in [1, 0]:
            outp_pn = x * self.weights[0] + self.bias * self.weights[2]
            # Based on the trained weights
            outp = 1.0 / (1 + numpy.exp(-outp_pn))
            print(str(x) + " " + self.operation + " yields: " + str(outp))
