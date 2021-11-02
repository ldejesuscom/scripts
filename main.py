import discord

client = discord.Client()

@client.event
async def on_ready():
  print("The bot is online and ready to roll!")

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.lower() == 'hello':  
      await message.channel.send('Welcome to Crypto Bot')

client.run('OTA0NTQ5NTI3MDk5NDI0ODMw.YX9JZA.vAsX-1a9vyemHJB4gbKPxAscFKA')