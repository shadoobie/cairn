import sys, json, unittest

sys.path.append('.')
sys.path.append('..')
from clovis_points.Flint import Flint
from the_historical_record.Block import Block
from the_historical_record.BlockChain import BlockChain




class TestStuff(unittest.TestCase):

    def test_the_historical_record(self):
        print("=======================================================================================================")
        print(" test_the_historical_record ")
        my_block_chain = BlockChain()
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
        or_perceptron = Flint(learning_rate, bias, operation)
        or_perceptron.train_2_inputs_1_output(iterations)

        print("==========================")
        operation = 'and'
        print(operation)
        print("==========================")
        iterations = 100
        or_perceptron = Flint(learning_rate, bias, operation)
        or_perceptron.train_2_inputs_1_output(iterations)

        print("==========================")
        operation = 'not'
        print(operation)
        print("==========================")
        iterations = 200
        not_perceptron = Flint(learning_rate, bias, operation)
        not_perceptron.train_1_input_to_1_output(iterations)

        # TODO need assertions and rounding to verify the NNs approached either 0 or 1 correctly.
        print("test_flint_perceptrons passes but needs assertions")
        print("=======================================================================================================")
        pass

    def test_json_nn_learning_snapshot_schema_loads(self):
        # TODO: this test needs a lot of tlc, schema specific validation and object validation to the schema
        print("=======================================================================================================")
        print(" test_json_nn_learning_snapshot_schema_loads ")
        data = None
        thing = None
        nn_snapshot_object = None
        nn_snapshot_schema = None

        json_schema = "C://Users//Owner//workspaces//cairn//resources//nn_learning_snapshot.schema.json"
        json_object_thing = "C://Users//Owner//workspaces//cairn//resources//nn_learning_snapshot.json"
        # read json schema file
        with open(json_schema) as myfile:
            data = myfile.read()

        if data is not None:
            try:
                nn_snapshot_schema = json.loads(data)
                # self.fail("hahahahahah")
                print("test_json_nn_learning_snapshot_schema_loads passes, schema is apparently valid json.")

            except ValueError:
                print("ValueError thrown when trying to load json schema file ( " + json_schema + " )")
            except AttributeError:
                print("AttributeError when trying to load json schema file ( " + json_schema + " )")
            except:
                print("something else went wrong when trying to load json schema file ( " + json_schema + " )")

        with open(json_object_thing) as thingfile:
            blah = thingfile.read()
            nn_snapshot_object = json.loads(blah)


        print("=======================================================================================================")
        pass


if __name__ == '__main__':
    unittest.main()
