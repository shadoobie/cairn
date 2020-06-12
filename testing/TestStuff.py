import sys
sys.path.append('.')
sys.path.append('..')
from clovis_points.Flint import Flint
from the_historical_record.Block import Block
from the_historical_record.BlockChain import BlockChain


class TestStuff:

    def __init__(self):
        print("TestStuff object instantiated. Running visual confirmation tests. Need a real test framework but this will do for now.")

    def test_the_historical_record(self):
        my_block_chain = BlockChain()
        for n in range(10):
            my_block_chain.mine(Block("Block " + str(n + 1)))
        while my_block_chain.head is not None:
            print(my_block_chain.head)
            my_block_chain.head = my_block_chain.head.next
        pass

    def test_flint_perceptrons(self):
        learning_rate = 1
        bias = 1
        operation = 'or'
        print("==========================")
        print(operation)
        print("==========================")
        iterations = 50
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


if __name__ == '__main__':
    test_stuff = TestStuff()
    print("========= Testing Simple Neural Networks Doing Some Logic ============")
    test_stuff.test_flint_perceptrons()
    print("========= Testing Simple Block Chain============")
    test_stuff.test_the_historical_record()
