import discord
from pycoingecko import CoinGeckoAPI
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/53298ef4473f41dab399d84ff234f0e7"
infura_url2 = "https://arbitrum-mainnet.infura.io/v3/53298ef4473f41dab399d84ff234f0e7"
web3 = Web3(Web3.HTTPProvider(infura_url))
web3arb = Web3(Web3.HTTPProvider(infura_url2))
wallet = web3.toChecksumAddress("0x48D8CB276C8340B55AFf89E077916594FA356fe7")

cg = CoinGeckoAPI()
client = discord.Client()

@client.event
async def on_ready():
  print("The bot is online and ready to roll!")

@client.event
async def on_message(message):
  
  msg = message.content.lower()

  if message.author == client.user:
    return

  if msg == 'hello':  
    await message.channel.send('Welcome to Crypto Bot')
  
  if msg == 'eth':
    eth_raw = web3.eth.getBalance(wallet)
    eth_balance = float(web3.fromWei(eth_raw, 'ether'))
    price = float(cg.get_price(ids = 'ethereum', vs_currencies = 'usd')['ethereum']['usd'])
    print(price)
    await message.channel.send(f'You have {"{:.2f}".format(eth_balance)} ETH worth ${"{:.2f}".format(eth_balance * price)}')
  
  if msg == 'ens':
    ens_tokens = 51
    price = float(cg.get_price(ids = 'ethereum-name-service', vs_currencies = 'usd')['ethereum-name-service']['usd'])
    print(price)
    await message.channel.send(f'You have {"{:.2f}".format(ens_tokens)} ENS worth ${"{:.2f}".format(ens_tokens * price)}')
  
  if msg == 'dev':
    dev_nonce = web3arb.eth.get_transaction_count("0x8602EE2f8AaEb671E409b26d48E36DD8Cc3B7ED7")
    print(dev_nonce)
    await message.channel.send(f'Nyan Dev Transaction Count: {dev_nonce}')
    
  if msg == 'whale1':
    whale_nonce = web3arb.eth.get_transaction_count("0x068f943adbae44c24e5A184010b4733F944b7f31")
    print(whale_nonce)
    await message.channel.send(f'Whale 1 Transaction Count: {whale_nonce}')
    
  if msg == 'whale2':
    whale2_nonce = web3arb.eth.get_transaction_count("0x930e9b64896431A24c84B3F95B91af3530Ae187F")
    print(whale2_nonce)
    await message.channel.send(f'Whale 2 Transaction Count: {whale2_nonce}') 
    

  else:
    price = cg.get_price(ids = msg, vs_currencies = 'usd')
    await message.channel.send(f"{msg} is ${price[msg]['usd']}")

client.run('OTA0NTQ5NTI3MDk5NDI0ODMw.YX9JZA.lbxdTIuebVzhXa3HjKu0pNOj0Bg')