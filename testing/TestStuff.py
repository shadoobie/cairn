import sys, json, jsonschema, unittest, the_historical_record

from testing.TestUtilities import TestUtilities

sys.path.append('.')
sys.path.append('..')

import clovis_points.Flint
from the_historical_record.Block import Block
from the_historical_record import BlockChain
from jsonschema import validate


class TestStuff(unittest.TestCase):
    utils = TestUtilities()

    def test_the_historical_record(self):
        print("=======================================================================================================")
        print(" test_the_historical_record ")
        my_block_chain = the_historical_record.BlockChain.BlockChain()
        for n in range(10):
            my_block_chain.mine(Block("Block " + str(n + 1)))
        while my_block_chain.head is not None:
            print(my_block_chain.head)
            my_block_chain.head = my_block_chain.head.next

        print("test_the_historical_record mined a hash,test passes, but needs assertions.")
        print("=======================================================================================================")
        pass

    def test_flint_perceptrons(self):

        print("=======================================================================================================")
        print(" test_flint_perceptrons ")

        learning_rate = 1
        bias = 1
        operation = 'or'
        print("==========================")
        print(operation)
        print("==========================")
        iterations = 200
        or_perceptron = clovis_points.Flint.Flint(learning_rate, bias, operation)
        or_perceptron.train_2_inputs_1_output(iterations)
        or_perceptron.use_perceptron_with_two_inputs_and_one_output()

        print("==========================")
        operation = 'and'
        print(operation)
        print("==========================")
        iterations = 100
        and_perceptron = clovis_points.Flint.Flint(learning_rate, bias, operation)
        and_perceptron.train_2_inputs_1_output(iterations)
        and_perceptron.use_perceptron_with_two_inputs_and_one_output()


        print("==========================")
        operation = 'not'
        print(operation)
        print("==========================")
        iterations = 200
        not_perceptron = clovis_points.Flint.Flint(learning_rate, bias, operation)
        not_perceptron.train_1_input_to_1_output(iterations)
        not_perceptron.use_perceptron_with_one_input_and_one_output()

        # TODO need assertions and rounding to verify the NNs approached either 0 or 1 correctly.
        print("test_flint_perceptrons passes but needs assertions")
        print("=======================================================================================================")
        pass

    def test_nn_learning_snapshot_valid_against_schema(self):
        # TODO: this test needs a lot of tlc, schema specific validation and object validation to the schema
        print("=======================================================================================================")
        print(" test_nn_learning_snapshot_valid_against_schema ")

        # first open the schema file into a data string object and
        nn_learning_snapshot_schema_location = "C://Users//Owner//workspaces//cairn//resources//nn_learning_snapshot.schema.json"
        schema_data = ""
        with open(nn_learning_snapshot_schema_location) as schema_file:
            nn_snapshot_schema = self.utils.load_json_file(schema_file)
            print('successfully loaded: ' + nn_learning_snapshot_schema_location)

            nn_learning_snapshot_object_to_validate_against_schema_location = "C://Users//Owner//workspaces//cairn//resources//nn_learning_snapshot.json"
            with open(nn_learning_snapshot_object_to_validate_against_schema_location) as object_file:
                nn_snapshot_object = self.utils.load_json_file(object_file)
                print('successfully loaded: ' + nn_learning_snapshot_object_to_validate_against_schema_location)
                validate(nn_snapshot_object, nn_snapshot_schema)
                print("validating " + nn_learning_snapshot_object_to_validate_against_schema_location +
                      " against the schema file " +
                      nn_learning_snapshot_schema_location +
                      " and since you're seeing this, i think it's considered valid.")
                print("test_nn_learning_snapshot_valid_against_schema done.")

        print("=======================================================================================================")
        pass


if __name__ == '__main__':
    unittest.main()
