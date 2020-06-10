import sys
sys.path.append('.')
sys.path.append('..')

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


if __name__ == '__main__':
    test_stuff = TestStuff()
    test_stuff.test_the_historical_record()
