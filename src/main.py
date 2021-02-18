from decouple import config
from discord.ext import commands

# Add the token of the bot
DISCORD_TOKEN = config("BOT_TOKEN")

# Description and basic configuration
description = "An helper bot for discord of Hola Mundo Community"
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)


# Bot initial config
@bot.event
async def on_ready():
    print(f"Initial as {bot.user}")


# Load the extensions
bot.load_extension("cogs.ping")
bot.load_extension("cogs.avatar")
bot.load_extension("cogs.quotes")
bot.load_extension("cogs.cat_facts")
bot.load_extension("cogs.dogs")
# Running the bot
bot.run(DISCORD_TOKEN)
