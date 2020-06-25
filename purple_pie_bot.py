# bot.py
import os

import discord
from dotenv import load_dotenv

# Loads env variables, mainly the DISCORD_TOKEN
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#logs to the console when connection is succesfully made
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#On message detect, check if the words "purple pie" are in the message. If they are >> kick the user and delete the purple pie message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower();

    if "purple pie" in msg or "purplepie" in msg:
        await message.delete(delay=None)
        await message.channel.send('My apologies. I have removed the infection.', tts=True)
        await message.guild.kick(message.author)

client.run(TOKEN)
