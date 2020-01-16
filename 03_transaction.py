from web3 import Web3

# Local blockchain
GANACHE_URL = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

address_1 = "" # Fill in
address_2 = "" # Fill in
private_key = "" # Fill in

nonce = web3.eth.getTransactionCount(address_1)

tx = {
        "nonce": nonce,
        "to": address_2,
        "value": web3.toWei(1, "ether"),
        "gas": 2000000,
        "gasPrice": web3.toWei("50", "gwei"),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
