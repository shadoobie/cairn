import sys, json, jsonschema, unittest, the_historical_record

from testing.TestUtilities import TestUtilities

sys.path.append('.')
sys.path.append('..')

from clovis_points.Flint import Flint
from the_historical_record.Block import Block
from the_historical_record import BlockChain
from utializers.ToiletChairLogFactory import ToiletChairLogFactory
from utializers.generatorfunctions import my_gen
from jsonschema import validate


class TestStuff(unittest.TestCase):
    utils = TestUtilities()
    log = ToiletChairLogFactory().get_logger("TestStuff", "_testing_stuff.log")

    def test_generator_functions(self):
        print("about to run my_gen()")
        my_gen()
        print("okay ran my_gen() what gives?")

    def test_the_historical_record(self):
        self.log.info(
            "=======================================================================================================")
        self.log.info(" test_the_historical_record ")
        my_block_chain = the_historical_record.BlockChain.BlockChain()
        for n in range(10):
            my_block_chain.mine(Block("Block " + str(n + 1)))
        while my_block_chain.head is not None:
            self.log.info(my_block_chain.head)
            my_block_chain.head = my_block_chain.head.next

        self.log.info("test_the_historical_record mined a hash,test passes, but needs assertions.")
        self.log.info(
            "=======================================================================================================")
        pass

    def test_flint_perceptrons(self):

        self.log.info(
            "=======================================================================================================")
        self.log.info(" test_flint_perceptrons ")

        learning_rate = 1
        bias = 1


        operation = 'or'
        self.log.info("==========================")
        self.log.info(operation)
        self.log.info("==========================")
        iterations = 200
        or_perceptron = Flint(learning_rate, bias, operation, self.log)
        or_perceptron.train_2_inputs_1_output(iterations)
        or_perceptron.use_perceptron_with_two_inputs_and_one_output()

        self.log.info("==========================")
        operation = 'and'
        self.log.info(operation)
        self.log.info("==========================")
        iterations = 100
        and_perceptron = Flint(learning_rate, bias, operation, self.log)
        and_perceptron.train_2_inputs_1_output(iterations)
        and_perceptron.use_perceptron_with_two_inputs_and_one_output()

        self.log.info("==========================")
        operation = 'not'
        self.log.info(operation)
        self.log.info("==========================")
        iterations = 200
        not_perceptron = Flint(learning_rate, bias, operation, self.log)
        not_perceptron.train_1_input_to_1_output(iterations)
        not_perceptron.use_perceptron_with_one_input_and_one_output()

        # TODO need assertions and rounding to verify the NNs approached either 0 or 1 correctly.
        self.log.info("test_flint_perceptrons passes but needs assertions")
        self.log.info(
            "=======================================================================================================")
        pass

    def test_nn_learning_snapshot_valid_against_schema(self):
        # TODO: this test needs a lot of tlc, schema specific validation and object validation to the schema
        self.log.info(
            "=======================================================================================================")
        self.log.info(" test_nn_learning_snapshot_valid_against_schema ")

        # first open the schema file into a data string object and
        nn_learning_snapshot_schema_location = "../resources/nn_learning_snapshot.schema.json"
        schema_data = ""
        with open(nn_learning_snapshot_schema_location) as schema_file:
            nn_snapshot_schema = self.utils.load_json_file(schema_file)
            self.log.info('successfully loaded: ' + nn_learning_snapshot_schema_location)

            nn_learning_snapshot_object_to_validate_against_schema_location = "../resources/nn_learning_snapshot.json"
            with open(nn_learning_snapshot_object_to_validate_against_schema_location) as object_file:
                nn_snapshot_object = self.utils.load_json_file(object_file)
                self.log.info('successfully loaded: ' + nn_learning_snapshot_object_to_validate_against_schema_location)
                validate(nn_snapshot_object, nn_snapshot_schema)
                self.log.info("validating " + nn_learning_snapshot_object_to_validate_against_schema_location +
                              " against the schema file " +
                              nn_learning_snapshot_schema_location +
                              " and since you're seeing this, i think it's considered valid.")

            nn_learning_snapshot_example_location = "../resources/random_or_nn_snapshot_sample_generated_in_the_log_in_test.json"
            self.run_schema_validation_for(nn_learning_snapshot_example_location, nn_snapshot_schema, nn_learning_snapshot_schema_location)

            nn_learning_snapshot_example_location = "../resources/random_and_nn_snapshot_sample_generated_in_the_log_in_test.json"
            self.run_schema_validation_for(nn_learning_snapshot_example_location, nn_snapshot_schema, nn_learning_snapshot_schema_location)

            nn_learning_snapshot_example_location = "../resources/random_not_nn_snapshot_sample_generated_in_the_log_in_test.json"
            self.run_schema_validation_for(nn_learning_snapshot_example_location, nn_snapshot_schema, nn_learning_snapshot_schema_location)

        self.log.info("test_nn_learning_snapshot_valid_against_schema done.")
        self.log.info(
            "=======================================================================================================")
        pass

    def run_schema_validation_for(self, nn_learning_snapshot_example_location, nn_snapshot_schema, nn_learning_snapshot_schema_location):

        with open(nn_learning_snapshot_example_location) as example_file:
            nn_sh_example = self.utils.load_json_file(example_file)
            validate(nn_sh_example, nn_snapshot_schema)
            self.log.info(
                "validating the generated learning snapshot example " + nn_learning_snapshot_example_location +
                " against the schema file " +
                nn_learning_snapshot_schema_location +
                " and since you're seeing this, i think it's considered valid.")

if __name__ == '__main__':
    unittest.main()
