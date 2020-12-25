import settings
import cog
from discord.ext import commands

bot = commands.Bot(command_prefix=settings.prefix)  # YOUR PREFIX HERE
bot.add_cog(cog.Mudae(bot))
bot.run(settings.token)  # YOUR TOKEN HERE
