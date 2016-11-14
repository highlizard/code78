import discord
from discord.ext import commands

class Weekday:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sunday(self):
        """This does stuff!"""

        await self.bot.say("Hello Sunday!")
    @commands.command()
    async def monday(self):
        """This does stuff!"""

        await self.bot.say("Hello Monday!")

    @commands.command()
    async def tuesday(self):
        """This does stuff!"""

        await self.bot.say("Hello Tuesday!")

    @commands.command()
    async def wednesday(self):
        """This does stuff!"""

        await self.bot.say("Hello Wednesday!")

    @commands.command()
    async def thursday(self):
        """This does stuff!"""

        await self.bot.say("Hello Thursday!")

    @commands.command()
    async def friday(self):
        """This does stuff!"""

        await self.bot.say("Hello Friday!")

    @commands.command()
    async def saturday(self):
        """This does stuff!"""

        await self.bot.say("Hello Saturday!")


def setup(bot):
    bot.add_cog(Weekday(bot))
