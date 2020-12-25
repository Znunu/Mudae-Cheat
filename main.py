import settings
import cog
from discord.ext import commands

bot = commands.Bot(command_prefix=settings.prefix)  # YOUR PREFIX HERE e.g. bot = commands.Bot(command_prefix="! ")
bot.add_cog(cog.Mudae(bot))
bot.run(settings.token)  # YOUR TOKEN HERE e.g. bot.run("ABCDEFSDS3434334")
