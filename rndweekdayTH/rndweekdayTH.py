from discord.ext import commands
import random
import discord
import datetime

class WeekdayTH:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
          
    @commands.command(pass_context=True)
    async def sun(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.name
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def mon(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def tue(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def wed(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def tur(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def fri(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

    @commands.command(pass_context=True)
    async def sat(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** '
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 1,2,3,4,5,6,7,8,9,10,11,12):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')

def setup(bot):
    bot.add_cog(WeekdayTH(bot))