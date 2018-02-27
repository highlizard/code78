import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class Nyaabuff:

    """Airenkun's Insult Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.nyaabuff = fileIO("data/nyaabuff/nyaabuff.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def nyaabuff(self, ctx, user : discord.Member=None):
        """Give A Nyaa buff to users"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "feels your Nyaa"
                await self.bot.say(user.name + msg)
            else:
                await self.bot.say(user.name + msg + randchoice(self.nyaabuff))
        else:
            await self.bot.say(ctx.message.author.mention + msg + randchoice(self.nyaabuff))


def setup(bot):
    bot.add_cog(Nyaabuff(bot))
