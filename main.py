import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import platform
import time
import colorsys
import random
prefix = "§"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print("Created by Captain Cool")
    print("Trivia Savage Pro:")
    print("https://discord.gg/cKQGjsS")
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Trivia!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Created by Cool"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with My server"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with All Users"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Happy moment"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Love"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="With Animals"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Kings"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with your Love😍!"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with All cmds!"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=2,name="with req.owner role"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  members!"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(5)

@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
bot.run("your_self_token",bot=False)
