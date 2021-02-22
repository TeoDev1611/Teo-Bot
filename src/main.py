from decouple import config
from discord.ext import commands

# Add the token of the bot
DISCORD_TOKEN = config("BOT_TOKEN")

# Description and basic configuration
description = "Un Bot de Ayuda para quien lo Necesite"
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)


# Bot initial config
@bot.event
async def on_ready():
    print(f"Initial as {bot.user}")


# Load the extensions
bot. load_extension("cogs.ping")
bot. load_extension("cogs.avatar")
bot. load_extension("cogs.quotes")
bot. load_extension("cogs.cat_facts")
bot. load_extension("cogs.dogs")
bot. load_extension("cogs.moderation")
bot.load_extension("cogs.invitacion")
# Running the bot
bot.run(DISCORD_TOKEN)
