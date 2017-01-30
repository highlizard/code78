import discord
import random
from discord.ext import commands

class WeekdayTH:
    """สวัสดีวันอาทิตย์ - วันเสาร์!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sun(self):
        """Hello Sunday!"""

        await self.bot.say(":rose: สวัสดีวันอาทิตย์! :rose:")
        
    @commands.command()
    async def mon(self):
        """Hello Monday!"""

        await self.bot.say(":hatched_chick: สวัสดีวันจันทร์! :hatched_chick:")

    @commands.command()
    async def tue(self):
        """Hello Tuesday!"""

        await self.bot.say(":cherry_blossom: สวัสดีวันอังคาร! :cherry_blossom:")

    @commands.command()
    async def wed(self):
        """Hello Wednesday!"""

        await self.bot.say(":four_leaf_clover: สวัสดีวันพุธ! :four_leaf_clover:")

    @commands.command()
    async def thu(self):
        """Hello Thursday!"""

        await self.bot.say(":tangerine: สวัสดีวันพฤหัสบดี! :tangerine: ")

    @commands.command()
    async def fri(self):
        """Hello Friday!"""

        await self.bot.say(":butterfly: สวัสดีวันศุกร์! :butterfly:")

    @commands.command()
    async def sat(self):
        """Hello Saturday!"""

        await self.bot.say(":grapes: สวัสดีวันเสาร์! :grapes:")


def setup(bot):
    bot.add_cog(WeekdayTH(bot))
