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
    await ctx.send("🏓 Pong! MAX BOT працює!")@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋│привітання")

    if channel:
        await channel.send(
            f"🇺🇦 Вітаємо, {member.mention}!\n\n"
            "🚜 Ласкаво просимо до **MAX FARMING UKRAINE**!\n\n"
            "📖 Ознайомся з правилами сервера.\n"
            "💬 Приємного спілкування та гарної гри!"
        )

bot.run(TOKEN)
