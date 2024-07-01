import settings
import cog
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="YOUR PREFIX HERE")

bot.add_cog(cog.Mudae(bot))

# UNCOMMENT THIS FOR BOT
# bot.run("YOUR TOKEN HERE", intents=discord.Intents.all())

# UNCOMMENT THIS FOR USER BOT
# bot.login("YOUR TOKEN HERE", bot=false, intents=discord.Intents.all())
