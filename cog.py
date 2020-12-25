from discord.ext import commands
import discord
import EzMudae
import winsound
import asyncio


class Mudae(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.muda = EzMudae.Mudae(bot)
        self.limit = 500  # REPLACE WITH YOUR OWN KAKERA THRESHOLD

    # REPLACE WITH YOUR OWN ALERT
    def alert(self):
        for _ in range(3):
            winsound.MessageBeep(winsound.MB_ICONHAND)
            asyncio.sleep(0.3)
        winsound.MessageBeep()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        waifu = self.muda.waifu_from(message)
        if waifu and waifu.kakera > self.limit: self.alert()