import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$Luke'):
        await message.channel.send('Age 5')
        
    if message.content.startswith('$whip'):
        await message.channel.send('Nay Nay')        

if os.environ.get('DISCORD_TOKEN') != None:
    client.run(os.environ.get('DISCORD_TOKEN'))
else:
    print("Exiting no valid token")