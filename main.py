import settings
import cog
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="YOUR PREFIX HERE", intents=discord.Intents.all())

bot.add_cog(cog.Mudae(bot))

bot.run("YOUR TOKEN HERE")
