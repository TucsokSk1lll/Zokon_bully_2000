import discord
from discord.ext import commands
from discord import app_commands
import discord_bot_token

# Create an instance of your bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your guild's ID
GUILD_ID = 881507710993063936  # Replace this with your actual guild ID

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # Sync the commands to a specific guild
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print(f"Synced commands to guild: {GUILD_ID}")

@bot.tree.command(name="greet", guild=discord.Object(id=GUILD_ID))  # Register command to specific guild
@app_commands.describe(name="Your name", times="How many times to greet")
async def greet(interaction: discord.Interaction, name: str, times: int):
    """A command to greet a user multiple times."""
    greeting = f"Hello, {name}!" * times
    await interaction.response.send_message(greeting)

bot.run(discord_bot_token.discord_bot_token)
