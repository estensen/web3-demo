import os
import sys

from web3 import Web3

if not (INFURA_API_KEY := os.getenv("INFURA_API_KEY")):
    print("INFURA_API_KEY env var is not set")
    sys.exit(0)

# Mainnet is where the real money is
INFURA_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# In case address is mistyped
checksum_address = Web3.toChecksumAddress("0xc6de9ebdd8e3cce618b56246029dbf11b052b462")
balance = web3.eth.getBalance(checksum_address)
print(balance)

