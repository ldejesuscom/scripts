# import Web3 library
from web3 import Web3
# Declare Infura Arbitrum MainNet API URL and set HTTP JSON RPC provider
infura_url = "https://arbitrum-mainnet.infura.io/v3/53298ef4473f41dab399d84ff234f0e7"
web3 = Web3(Web3.HTTPProvider(infura_url))

print("ArbiNyan Deployer Account:")
print(web3.eth.get_transaction_count("0x8602EE2f8AaEb671E409b26d48E36DD8Cc3B7ED7"))

print("\n\nArbiNyan Whale Account 1:")
print(web3.eth.get_transaction_count("0x068f943adbae44c24e5A184010b4733F944b7f31"))

print("\n\nArbiNyan Whale Account 2:")
print(web3.eth.get_transaction_count("0x930e9b64896431A24c84B3F95B91af3530Ae187F"))
