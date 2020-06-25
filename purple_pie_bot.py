# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

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
