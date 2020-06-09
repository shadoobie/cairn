from the_historical_record.Block import Block


class BlockChain:
    diff = 20
    maxNonce = 2 ** 20
    target = 2 ** (256 - diff)

    block = Block("genesis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

# if __name__ == '__main__':
#     myBlockChain = BlockChain()
#
#     for n in range(10):
#         myBlockChain.mine(Block("Block " + str(n + 1)))
#
#     while myBlockChain.head is not None:
#         print(myBlockChain.head)
#         myBlockChain.head = myBlockChain.head.next
