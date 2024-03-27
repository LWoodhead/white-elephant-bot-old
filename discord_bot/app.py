import discord
import os
from classes.identifierGenerator import IdentifierGenerator
from discord.commands import Option

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.slash_command()
async def create_game(ctx):
    # TODO create a unique id. create a gamewrapper object
    game_id = IdentifierGenerator.generateGameIdentifier()
    await ctx.respond(f"Game {game_id} Created")
    
@bot.slash_command()
async def add_player(ctx):
    await ctx.respond("Player Added")
    
@bot.slash_command(name='config', description='Chose a default game config')
async def set_config(ctx: discord.ApplicationContext, config: Option(str, 'config value', required = False, default = '')): # type: ignore
    await ctx.respond(config)
    
@bot.slash_command()
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("Pong")
    
@bot.slash_command()
async def whip(ctx):
    await ctx.respond("Nay Nay")      

if os.environ.get('DISCORD_TOKEN') is not None:
    bot.run(os.environ.get('DISCORD_TOKEN'))
else:
    print("Exiting no valid token")