from discord.ext import commands
import discord

class hola_command(commands.Cog):
	def __init_(self, bot):
        self.bot = bot

    @commands.command(
    	name = "hola",
    	usage = "",
    	description = "Te voy a saludar")
    async def hola(self,ctx):
    	embed = discord.Embed(
    		title = "Hola como estas?",
    		description = "Nota: Estoy vivo xd",
    		color = discord.Color.random()
    		)
    	await ctx.send(embed=embed)
    	
def setup(bot):
	bot.add_cog(hola_command(bot))