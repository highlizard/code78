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

        await self.bot.say(":rose: สวัสดีวันอาทิตย์ ขอให้จิตสดใส! :rose:")
        
    @commands.command()
    async def mon(self):
        """Hello Monday!"""

        await self.bot.say(":hatched_chick: สวัสดีวันจันทร์ ต้อนรับวันใหม่ :hatched_chick:")

    @commands.command()
    async def tue(self):
        """This does stuff!"""

        await self.bot.say(":cherry_blossom: สวัสดีวันอังคาร ใจใสเบิกบาน! :cherry_blossom:")

    @commands.command()
    async def wed(self):
        """This does stuff!"""

        await self.bot.say(":four_leaf_clover: สวัสดีวันพุธ ดีสุดสุดวันพุธสดใส! :four_leaf_clover:")

    @commands.command()
    async def thu(self):
        """This does stuff!"""

        await self.bot.say(":tangerine: สวัสดีวันพฤหัสบดี ขอให้ทุกท่านมีความสุข! :tangerine: ")

    @commands.command()
    async def fri(self):
        """This does stuff!"""

        await self.bot.say(":butterfly: สวัสดีวันศุกร์ ขอให้มีความสุขกันทั้งวัน! :butterfly:")

    @commands.command()
    async def sat(self):
        """This does stuff!"""

        await self.bot.say(":grapes: สวัสดีวันเสาร์ ไม่เหงาไม่เศร้า! :grapes:")


def setup(bot):
    bot.add_cog(WeekdayTH(bot))
