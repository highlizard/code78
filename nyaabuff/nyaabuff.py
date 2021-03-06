import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
import os

defaults = [
    "HP",
    "MP",
    "Physical Damage",
    "Magical Damage",
    "Physical Critical Damage",
    "Magical Critical Damage",
    "Physical Critical Rate",
    "Magical Critical Rate",
    "Physical Defense Penetration",
    "Magical Defense Penetration",
    "Physical Defense",
    "Magical Defense",
    "Skill Cooldown Reduction",
    "Skill Cost Reduction",
    "Attack Speed",
    "Movement Speed",
    "Phase Power Charge Rate",
    "Phase Power Release Duration",
    "Phase Power Release Damage Boost",
    "Additional Damage during Aerial Attacks",
    "Critical Rate during Aerial Attacks",
    "Defense Penetration Rate during Aerial Attacks",
    "Critical Damage during Aerial Attacks",
    "Additional Damage during Back Attacks",
    "Critical Rate during Back Attacks",
    "Defense Penetration Rate during Back Attacks",
    "Critical Damage during Back Attacks",
    "Additional Damage during Chase Attacks",
    "Critical Rate during Chase Attacks",
    "Defense Penetration Rate during Chase Attacks",
    "Critical Damage during Chase Attacks",
    "Additional Credits",
    "Additional Item Drop Rate",
    "Additional Experience",
    "HP Regenerated per 3 Seconds",
    "MP Regenerated per 3 Seconds",]
    

class Nyaabuff:
    """Give Nyaa buff"""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/nyaabuff/nyaalist.json", "load")

    @commands.command()
    async def feed(self, user : discord.Member=None):
        """buff by NyaaNook"""
        if user.id == self.bot.user.id:
            await self.bot.say("Feels your Nyaa")
            return
        await self.bot.say("-your {} increased {} was"
                           " buff".format(rndchoice(self.items),
                                             user.name))

def check_folders():
    if not os.path.exists("data/nyaabuff"):
        print("Creating data/nyaabuff folder...")
        os.makedirs("data/feed")

def check_files():
    f = "data/nyaabuff/nyaalist.json"
    if not fileIO(f, "check"):
        print("Creating empty nyaalist.json...")
        fileIO(f, "save", defaults)


def setup(bot):
    check_folders()
    check_files()
    n = Nyaabuff(bot)
    bot.add_cog(n)
