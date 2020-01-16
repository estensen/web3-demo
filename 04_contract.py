import json

from web3 import Web3

# Local blockchain
GANACHE_URL = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# Set pre-funded account as sender
web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('')  # Fill in

bytecode = ""  # Fill in

# Init contract
contract = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = contract.constructor().transact()
# Wait for the transaction to be mined
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

greeter = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

greeting = greeter.functions.greet().call()
print(greeting)

tx_hash = greeter.functions.setGreeting("Hello Håvard").transact()
web3.eth.waitForTransactionReceipt(tx_hash)

new_greeting = greeter.functions.greet().call()
print(new_greeting)

