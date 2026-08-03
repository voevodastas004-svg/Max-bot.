import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} успішно запущений!")
    await bot.change_presence(
        activity=discord.Game(name="🚜 MAX FARMING UKRAINE")
    )

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! MAX BOT працює!")

bot.run(TOKEN)
