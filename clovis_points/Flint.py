import numpy, json
from numpy import random
import uuid
import the_historical_record
from clovis_points import ActivationFunctions as af
from clovis_points import TruthTables as tt
from testing.TestUtilities import TestUtilities
from the_historical_record.Block import Block


class Flint:
    learning_rate = 0  # (Lithic reduction)
    bias = 0
    weights = None
    truth_table = None
    operation = None
    training_ledger = None
    utils = None
    ledger_item_template = None
    learning_record_template = None
    data_header = None

    def __init__(self, learning_rate, bias, operation):
        self.utils = TestUtilities()
        self.learning_rate = learning_rate
        self.bias = bias
        self.truth_table = self.__determine_truth_table__(operation)
        self.weights = list()
        for k in range(3):
            self.weights.append(random.random())  # Assigning random weights

        self.training_ledger = the_historical_record.BlockChain.BlockChain()
        self.__init_historical_data__()

    def __determine_truth_table__(self, operation):
        #TODO: should probably put the truth table that this determines into the data header
        if operation in ['and', 'AND', 'And', '&']:
            self.operation = 'AND'
            return tt.TruthTables.and_truth_table()
        elif operation in ['or', 'OR', 'Or', '|']:
            self.operation = 'OR'
            return tt.TruthTables.or_truth_table()
        elif operation in ['not', 'NOT', 'Not', '-']:
            self.operation = 'NOT'
            return tt.TruthTables.not_truth_table()

    def __init_historical_data__(self):
        self.ledger_item_template = self.__init_ledger_item__()
        some_array_yo = self.ledger_item_template["learning_history"]
        self.learning_record_template = some_array_yo[0]
        self.data_header = self.__create_the_data_header__()
        self.data_header['id'] = str(uuid.SafeUUID)
        self.data_header['name'] = 'Flint Perceptron'
        self.data_header['nn_class'] = self.__class__.__name__
        self.data_header['operation'] = self.operation
        self.data_header['bias'] = self.bias
        self.data_header['activation_function_name'] = "Sigmoid function"
        self.data_header['activation_function'] = "s(x) = 1 / 1 + e^-x = e^x / e^x + 1"
        #TODO finish initializng the data header after clearing out the learning history from the header template

        if self.operation in ['and', 'or']:
            self.data_header['weight_modification_functions'] = ["w0 = w0 + error * input1 * learning_rate",
                                                                 "w1 = w1 + error * input2 * learning_rate",
                                                                 "w2 = w2 + error * bias * learning_rate"]
            self.data_header['weight_initialization_functions'] = ["random", "random", "random"]
            self.data_header['starting_weights'] = [self.weights[0], self.weights[1], self.weights[2]]
        elif self.operation in ['not']:
            self.data_header['weight_modification_functions'] = ["w0 = w0 + error * input1 * learning_rate",
                                                                 "w1 = w1 + error * bias * learning_rate"]
            self.data_header['weight_initialization_functions'] = ["random", "random"]
            self.data_header['starting_weights'] = [self.weights[0], self.weights[1]]
        self.data_header['learning_history'] = [] # this might be redundant and or the best way to do this?

    def __init_ledger_item__(self):
        a_ledger_item = None
        item_data_structure_location = "..//resources//nn_learning_snapshot.json"
        #TODO: need to bring the schema in with it and validate it before proceeding.
        with open(item_data_structure_location) as item_data_structure:
            a_ledger_item = self.utils.load_json_file(item_data_structure)
            print('successfully loaded: ' + item_data_structure_location)

        return a_ledger_item

    def __create_the_data_header__(self):
        header = self.ledger_item_template.copy()
        learning_history = header["learning_history"]
        # clear out the learning history
        del learning_history[0]
        return header

    def create_a_learning_record(self):
        return self.learning_record_template.copy()

    def calculate_error_for_two_inputs_one_output(self, input1, input2, expected_output):
        actual_output = af.ActivationFunctions.sigmoid_function_dual_inputs(input1,
                                                                            input2,
                                                                            self.bias,
                                                                            self.weights)
        error = expected_output - actual_output
        return [error, actual_output]

    def calculate_error_for_one_input_one_output(self, input1, expected_output):
        sigmoid_output = af.ActivationFunctions.sigmoid_function_single_input(input1,
                                                                              self.bias,
                                                                              self.weights)
        error = expected_output - sigmoid_output
        return error

    def modify_weights_training(self, error, input1, input2):
        self.weights[0] += error * input1 * self.learning_rate
        self.weights[1] += error * input2 * self.learning_rate
        self.weights[2] += error * self.bias * self.learning_rate

    def calculate_error_and_modify_weights_for_case(self, case):
        error_and_actual = self.calculate_error_for_two_inputs_one_output(self.truth_table[case].get('input1'),
                                                               self.truth_table[case].get('input2'),
                                                               self.truth_table[case].get('expected_output'))

        self.modify_weights_training(error_and_actual[0],
                                     self.truth_table[case].get('input1'),
                                     self.truth_table[case].get('input2'))
        return error_and_actual

    def calculate_error_and_modify_weights_for_not(self, case):
        error = self.calculate_error_for_one_input_one_output(self.truth_table[case].get('input1'),
                                                              self.truth_table[case].get('expected_output'))
        self.modify_weights_training_for_not(error,
                                             self.truth_table[case].get('input1'))

    def modify_weights_training_for_not(self, error, input1):
        self.weights[0] += error * input1 * self.learning_rate
        self.weights[2] += error * self.bias * self.learning_rate

    #TODO: this whole thing sheesh man aww jeeze wow man i mean this is like a whole nother evening or somethign you know?
    def determine_if_perceptron_perceives_correctly_enough(self, mastery_criteria, i, iterations):
        mastered = False
        if (i > iterations - 3):
            mastered = True

        return mastered

    def train_2_inputs_1_output(self, iterations):
        for i in range(iterations):
            for n in range(4):
                case = 'case' + str(n + 1)
                error_and_actual = self.calculate_error_and_modify_weights_for_case(case)
                a_learning_record = self.create_a_learning_record()
                a_learning_record['id'] = case + ':' + self.data_header['id'] + ':' + str(uuid.SafeUUID)
                a_learning_record['iteration'] = i
                a_learning_record['metrics']['id'] = a_learning_record['id'] + ':' + str(uuid.SafeUUID)
                a_learning_record['metrics']['weights'] = self.weights
                if self.data_header['operation'] in ['and', 'or'] and self.operation in ['and', 'or']:
                    a_learning_record['metrics']['inputs'] = [self.truth_table[case].get('input1'), self.truth_table[case].get('input2')]
                elif self.data_header['operation'] in ['not'] and self.operation in ['not']:
                    a_learning_record['metrics']['inputs'] = [self.truth_table[case].get('input1')]
                a_learning_record['metrics']['expected_output'] = [self.truth_table[case].get('expected_output')]
                a_learning_record['metrics']['actual_output'] = [error_and_actual[1]] #TODO: consider making a two attribute class for this with good get names. or something.
                a_learning_record['metrics']['error'] = [error_and_actual[0]] #TODO: consider making a two attribute class for this with good get names. or something.
                a_learning_record['metrics']['mastered'] = False
                a_learning_record['metrics']['mastery_criteria'] = "who cares, for now when the iterations are done."
                a_learning_record['metrics']['mastered'] = self.determine_if_perceptron_perceives_correctly_enough(a_learning_record['metrics']['mastery_criteria'], i, iterations)
                self.data_header['learning_history'].append(a_learning_record)
            self.training_ledger.mine(Block(self.data_header.get('name') + str(self.data_header)))
        while self.training_ledger.head is not None:
            print(self.training_ledger.head)
            self.training_ledger.head = self.training_ledger.head.next



    def use_perceptron_with_two_inputs_and_one_output(self):
        for x, y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            output = af.ActivationFunctions.sigmoid_function_dual_inputs(x, y, self.bias, self.weights)
            print(str(x) + " " + self.operation + " " + str(y) + " yields: " + str(output))

    def train_1_input_to_1_output(self, iterations):
        for i in range(iterations):
            for n in range(2):
                case = 'case' + str(n + 1)
                self.calculate_error_and_modify_weights_for_not(case)

    def use_perceptron_with_one_input_and_one_output(self):
        for x in [1, 0]:
            output = af.ActivationFunctions.sigmoid_function_single_input(x, self.bias, self.weights)
            print(str(x) + " " + self.operation + " yields: " + str(output))