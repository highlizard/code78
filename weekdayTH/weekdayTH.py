import discord
import random
from discord.ext import commands

class WeekdayTH:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sun(self):
        """Hello Monday!"""

        await self.bot.say("สวัสดีวันอาทิตย์ ขอให้จิตสดใส")
        
    @commands.command()
    async def mon(self):
        """Hello Monday!"""

        await self.bot.say("สวัสดีวันจันทร์ ต้อนรับวันใหม่")

    @commands.command()
    async def tue(self):
        """This does stuff!"""

        await self.bot.say("Hello Tuesday!")

    @commands.command()
    async def wed(self):
        """This does stuff!"""

        await self.bot.say("Hello Wednesday!")

    @commands.command()
    async def thu(self):
        """This does stuff!"""

        await self.bot.say("Hello Thursday!")

    @commands.command()
    async def fri(self):
        """This does stuff!"""

        await self.bot.say("Hello Friday!")

    @commands.command()
    async def sat(self):
        """This does stuff!"""

        await self.bot.say("Hello Saturday!")


def setup(bot):
    bot.add_cog(WeekdayTH(bot))
