from discord.ext import commands
import discord 

class ping_command(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(
        name="ping",
        usage="",
        description = "El bot responde pong"
    )
    async def ping(self,ctx):
        embed = discord.Embed(
            title="Pong 🚀",
            color= discord.Color.blue(),
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(ping_command(bot))