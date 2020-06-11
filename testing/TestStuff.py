import sys
sys.path.append('.')
sys.path.append('..')
from clovis_points.Flint import Flint
from the_historical_record.Block import Block
from the_historical_record.BlockChain import BlockChain


class TestStuff:

    def __init__(self):
        print("why does init send pass?")

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
        iterations = 50
        or_perceptron = Flint(learning_rate, bias, operation)
        or_perceptron.train_2_inputs_1_output_(iterations)


if __name__ == '__main__':
    test_stuff = TestStuff()
    test_stuff.test_flint_perceptrons()
    # test_stuff.test_the_historical_record()
