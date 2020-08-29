import unittest
import json
from web3 import Web3

from infur.InfurUtils import InfurUtils


class TestInfer(unittest.TestCase):

    util = InfurUtils()

    def test_what_are_you_infuraing(self):
        infur_url = "https://mainnet.infura.io/v3/302093503f54409ab515af1c1b775a6c"
        web3 = Web3(Web3.HTTPProvider(infur_url))
        self.assertTrue(web3.isConnected(), "web3 isn't connected.")
        print("web3 is connected to " + infur_url)
        print("current block number: " + str(web3.eth.blockNumber))
        balance = web3.eth.getBalance("0x43778119cC6067C942d0E0729128d8691343339F")
        print("get balance: " + str(balance))
        print(web3.fromWei(balance, "ether"))

    def test_smart_contract_for_band_token(self):
        infur_url = "https://mainnet.infura.io/v3/302093503f54409ab515af1c1b775a6c"
        web3 = Web3(Web3.HTTPProvider(infur_url))
        self.assertTrue(web3.isConnected(), "web3 isn't connected.")
        print("web3 is connected to " + infur_url)

        band_token_abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"},{"name":"sig","type":"bytes4"},{"name":"data","type":"bytes"}],"name":"transferAndCall","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"votingPowerChangeNonce","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"votingPowerChangeCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"account","type":"address"}],"name":"addMinter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceMinter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"value","type":"uint256"}],"name":"burn","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"isMinter","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"nonce","type":"uint256"}],"name":"historicalVotingPowerAtNonce","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"index","type":"uint256"}],"name":"historicalVotingPowerAtIndex","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"account","type":"address"}],"name":"MinterAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"account","type":"address"}],"name":"MinterRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
        smart_contract_address = "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55"
        lower_case_and_lower_security_smart_contract_address = web3.toChecksumAddress(smart_contract_address)
        smart_contract = web3.eth.contract(address=lower_case_and_lower_security_smart_contract_address,
                                           abi=band_token_abi)
        total_supply_inwie = smart_contract.functions.totalSupply().call()
        print("the total supply of band tokens (in Wei?): " + str(total_supply_inwie))

        # Must be one of wei/kwei/babbage/femtoether/mwei/lovelace/picoether/gwei/shannon/nanoether/nano/szabo/microether/micro/finney/milliether/milli/ether/kether/grand/mether/gether/tether
        # total_supply_to18d = web3.fromWei(total_supply_inwie, 'ether / using 18 decimals.')
        # print("the total supply " + str(total_supply_to18d))

        print("Smart contract name:")
        print(smart_contract.functions.name().call())
        print("Smart contract token's ticker symbol:")
        print(smart_contract.functions.symbol().call())
        account_holder_address = web3.toChecksumAddress("0x7a62a7dcf64e1eb94e374ec187ad14ba6e595062")
        balance = smart_contract.functions.balanceOf(account_holder_address).call()
        print("balance of the largest account holder:")
        print(balance)

        adjusted_balance = self.util.from_wei(balance)
        print(adjusted_balance)








if __name__ == '__main__':
    unittest.main()
