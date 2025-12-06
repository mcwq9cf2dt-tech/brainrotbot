# bot.py
import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is online!")

bot.run(os.getenv("DISCORD_TOKEN"))
