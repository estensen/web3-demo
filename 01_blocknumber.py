import os
import sys

from web3 import Web3

if not (INFURA_API_KEY := os.getenv("INFURA_API_KEY")):
    print("INFURA_API_KEY env var is not set")
    sys.exit(0)

# Ropsten is the test net that most resemble the main net
INFURA_URL = f"https://ropsten.infura.io/v3/{INFURA_API_KEY}"

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

print(web3.eth.blockNumber)
"""
Double-check with Etherscan: https://etherscan.io/

`blockNumber` is not very Pythonic
Web3.py is derived from web3.js
"""

