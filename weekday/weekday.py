from discord.ext import commands
import random
import discord
import datetime

class Weekday:
    """Happy Weekday"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def newyear(self):
        """Hello Sunday!"""
        d = datetime.isoweekday.today()
        cweekday = date.isoweekday
        
        if ( cweekday == 1):
            await self.bot.say('**Happy Sunday**')
        else:
            await self.bot.say('**It isn\'t Sunday yet! Come back on Sunday!**')
    def setup(bot):
        bot.add_cog(Weekday(bot))
