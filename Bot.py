import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = command.Bot(command_prefix = "|")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "Hello":
        await client.send_message(message.channel, "Hello:)




client.login(process.env.BOT_TOKEN);
