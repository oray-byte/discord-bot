from http import client
from unicodedata import category
import discord
import os
import typing
from time import sleep
from discord.ext import commands as cmds
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = cmds.AutoShardedBot(cmds.when_mentioned_or('^'),help_command=None, intents=intents)


#Function: Adds a voice cannel to a category channel. 
@bot.command()
async def cvc(ctx, name):
    cata = discord.utils.get(ctx.guild.categories, name="Teams")
    print(ctx.guild.categories)
    await ctx.guild.create_voice_channel(name, category = cata)
    await ctx.send(f"{name} voice channel has been created")

#Function: Removes a voice cannel to a category channel. 
@bot.command()
async def dvc(ctx, name):
    cata = discord.utils.get(ctx.guild.categories, name="Teams")
    print(ctx.guild.categories)
    await ctx.guild.delete_voice_channel(name, category = cata) #dont know the actual code for this <---
    await ctx.send(f"{name} voice channel has been removed")

#Function: Bot repeats what you type. 
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

#Function: Bot repeats what you type 10 times. 
@bot.command()
async def spamTest(ctx, *, arg):
    for i in range(10): 
        await ctx.send(arg)
        sleep(1)

#Function: Bottles of beer song. 
@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 10, *, liquid="beer"):
    for amt in range(amount,0,-1):
        if amt!=1:
            await ctx.send(f'{amt} bottles of {liquid} on the wall! {amt} bottles of {liquid}! Take one down. Pass it around! {amt} bottles of {liquid} on the wall!')
        else:
            #singularity baby!!!
            await ctx.send(f'{amt} bottle of {liquid} on the wall! {amt} bottle of {liquid}! Take one down. Pass it around! {amt} bottle of {liquid} on the wall!')
        sleep(1)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


bot.run(TOKEN)

