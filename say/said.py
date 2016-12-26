from cogs.utils import checks
from discord.ext import commands


class Said:
    """I'll repeat what you said."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def said(self, *text):
        """I'll repeat what you said."""

        text = " ".join(text)
        await self.bot.say(text)

    @commands.command()
    async def sonar(self, channelid, *, text):
        """I'll repeat what you said and where you want it.
        A modified version of the debug command, with help from Calebj."""

        text = text.replace("\'", "\\\'")
        channelid = self.bot.get_channel(str(channelid))
        return await self.bot.send_message(channelid, text)

    @commands.command(pass_context=True)
    async def chinfo(self, ctx):
        """Gets current channel ID immediately."""
        channel = ctx.message.channel
        return await self.bot.say(channel.id)


def setup(bot):
    bot.add_cog(Said(bot))
