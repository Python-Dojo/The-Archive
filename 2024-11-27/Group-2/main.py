"""
Python Dojo Bot

- Create list of some ideas
- Function that returns a random string of text (that will be used for posting to the channel)
- Import the discord library
- create a discord client

https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

"""



import discord
import os
from discord.channel import TextChannel
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GENERAL_CHAT_ID = 1311407106976645162
OPTIONS = [
    "Hello there",
    "I am a discord bot",
]

if not TOKEN:
    raise EnvironmentError("Missing discord token")

intents = discord.Intents.default()
intents.message_content = True
client= discord.Client(intents=intents)

    
@client.event 
async def on_ready():
    print(f"{client.user} has joined the discord")
    general = client.get_channel(GENERAL_CHAT_ID)
    if isinstance(general, TextChannel):
        await general.send(f"{client.user} is in the house!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"hi {member.name}, welcome to the safest place on the internet")

@client.event
async def on_message(message):
    print(message)
    print(f"{message.content=}")
    if message.author == client.user:
        return
    if message.content == "test":
        response = "There has been a message"
        await message.channel.send(response)
    if message.content == "idea":
        response = "Loading idea..."
        await message.channel.send(response)

 
if __name__ == "__main__":
    client.run(TOKEN)