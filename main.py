import settings
import cog
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="YOUR PREFIX HERE", intents=discord.Intents.all())

bot.add_cog(cog.Mudae(bot))

# UNCOMMENT THIS FOR BOT
# bot.run("YOUR TOKEN HERE")

# UNCOMMENT THIS FOR USER BOT
# bot.login("YOUR TOKEN HERE", bot=false)
