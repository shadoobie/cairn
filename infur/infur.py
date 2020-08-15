import unittest
from web3 import Web3

class TestInfer(unittest.TestCase):
    def test_what_are_you_infuraing(self):
        infur_url = "https://mainnet.infura.io/v3/302093503f54409ab515af1c1b775a6c"
        web3 = Web3(Web3.HTTPProvider(infur_url))
        self.assertTrue(web3.isConnected(), "web3 isn't connected.")
        print("web3 is connected to " + infur_url)
        print("current block number: " + str(web3.eth.blockNumber))
        balance = web3.eth.getBalance("0x43778119cC6067C942d0E0729128d8691343339F")
        print("get balance: " + str(balance))
        print(web3.fromWei(balance, "ether"))



if __name__ == '__main__':
    unittest.main()
