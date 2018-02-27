import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os


class Nyaabuff:

    """Nyaa power"""
    def __init__(self, bot):
        self.bot = bot
        self.nyaabuffs = fileIO("data/nyaabuff/nyaabuffs.json","load")

    @commands.command(pass_context=True, no_pm=True)
    async def nyaabuff(self, ctx, user : discord.Member=None):
        """nyaabuff the user"""

        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "feel your Nyaa!"
                await self.bot.say(user.name + msg)
            else:
                await self.bot.say(user.name + msg + randchoice(self.nyaabuffs))
        else:
            await self.bot.say(ctx.message.author.name + msg + randchoice(self.nyaabuffs))


def setup(bot):
    bot.add_cog(Nyaabuff(bot))
