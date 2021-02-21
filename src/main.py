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
extensions = ["cogs.moderation", "cogs.dogs",
              "cogs.cat_facts", "cogs.quotes", "cogs.avatar", "cogs.ping"]

for i in extensions:
    try:
        bot.load_extension(i)
    except Exception as e:
        print("Ups a ocurrido un error")
        print(e)

# Running the bot
bot.run(DISCORD_TOKEN)
