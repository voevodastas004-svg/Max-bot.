
import os
import discord
from discord.ext import commands
from discord.ui import Button, View
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} успішно запущений!")
    await bot.change_presence(
        activity=discord.Game(name="🚜 Farming Simulator")
    )


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! MAX BOT працює!")


@bot.command()
async def testwelcome(ctx):
    await ctx.send(
        f"🇺🇦 Вітаємо, {ctx.author.mention}!\n\n"
        "🚜 Ласкаво просимо до **MAX FARMING UKRAINE**!\n\n"
        "📖 Ознайомся з правилами сервера.\n"
        "💬 Приємного спілкування та гарної гри!"
    )
@bot.command()
async def правила(ctx):
    await ctx.send(
        "📜 **Правила сервера MAX FARMING UKRAINE**\n"
        "1️⃣ Поважайте інших учасників.\n"
        "2️⃣ Заборонені образи та токсична поведінка.\n"
        "3️⃣ Не спамте.\n"
        "4️⃣ Не рекламуйте сторонні сервери.\n"
        "5️⃣ Дотримуйтесь правил адміністрації.\n"
        "🚜 Гарної гри!"
    )

@bot.command()
async def допомога(ctx):
    embed = discord.Embed(
        title="🤖 MAX BOT — Довідка",
        description="Ось список доступних команд:",
        color=discord.Color.green()
    )

    embed.add_field(
        name="🏓 !ping",
        value="Перевірка роботи бота.",
        inline=False
    )

    embed.add_field(
        name="👋 !testwelcome",
        value="Показує тестове привітання.",
        inline=False
    )

    embed.add_field(
        name="📜 !правила",
        value="Показує правила сервера.",
        inline=False
    )

    embed.add_field(
        name="❓ !допомога",
        value="Показує список команд.",
        inline=False
    )

    embed.set_footer(text="MAX FARMING UKRAINE 🚜")

    await ctx.send(embed=embed)
    await ctx.send(
        "📜 **Правила сервера MAX FARMING UKRAINE**\n\n"
        "1️⃣ Поважайте інших учасників.\n"
        "2️⃣ Заборонені образи та токсична поведінка.\n"
        "3️⃣ Не спамте.\n"
        "4️⃣ Не рекламуйте сторонні сервери.\n"
        "5️⃣ Дотримуйтесь правил адміністрації.\n"
        "🚜 Гарної гри!"
    )
class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🎫 Створити тікет", style=discord.ButtonStyle.green)
    async def create_ticket(self, button, interaction):
        await interaction.response.send_message(
            "✅ Функція тікетів скоро буде підключена!",
            ephemeral=True
        )

@bot.command()
async def ticket(ctx):
    embed = discord.Embed(
        title="🎫 Система тікетів",
        description="Натисніть кнопку нижче, щоб створити тікет.",
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed, view=TicketView())
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels,
        name="👋│привітання"
    )

    if channel:
        await channel.send(
            f"🇺🇦 Вітаємо, {member.mention}!\n\n"
            "🚜 Ласкаво просимо до **MAX FARMING UKRAINE**!\n\n"
            "📖 Ознайомся з правилами сервера.\n"
            "💬 Приємного спілкування та гарної гри!"
        )


bot.run(TOKEN)
