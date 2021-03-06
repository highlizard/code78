from discord.ext import commands

class closerspet:
	"""Closers pet command."""
	def __init__(self, bot):
		self.bot = bot
		self.base = 'data/closerspet/images/'

	@commands.command(pass_context=True)
	async def minibug(self, context):
	   	await self.bot.send_file(context.message.channel, '{}bug.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def penguin(self, context):
	   	await self.bot.send_file(context.message.channel, '{}penguin.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seha(self, context):
	   	await self.bot.send_file(context.message.channel, '{}seha.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seulbi(self, context):
	   	await self.bot.send_file(context.message.channel, '{}seulbi.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def levia(self, context):
		await self.bot.send_file(context.message.channel, '{}levia.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def selin(self, context):
		await self.bot.send_file(context.message.channel, '{}selin.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seha8(self, context):
		await self.bot.send_file(context.message.channel, '{}8seha.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seulbi8(self, context):
		await self.bot.send_file(context.message.channel, '{}8seulbi.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def yuri8(self, context):
		await self.bot.send_file(context.message.channel, '{}8yuri.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def mistel8(self, context):
		await self.bot.send_file(context.message.channel, '{}8misteltein.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def nata8(self, context):
		await self.bot.send_file(context.message.channel, '{}8nata.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def levia8(self, context):
		await self.bot.send_file(context.message.channel, '{}8levia.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def harpy8(self, context):
		await self.bot.send_file(context.message.channel, '{}8harpy.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def j8(self, context):
		"""J 8bit"""
		await self.bot.send_file(context.message.channel, '{}8J.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def vaccine(self, context):
		"""Vaccine -1"""
		await self.bot.send_file(context.message.channel, '{}Vaccine.PNG'.format(self.base))
			
	@commands.command(pass_context=True, aliases=[])
	async def washing(self, context):
		"""Wasting Machine"""
		await self.bot.send_file(context.message.channel, '{}washing.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def sehaok(self, context):
		"""Seha OK"""
		await self.bot.send_file(context.message.channel, '{}sehaok.png'.format(self.base))
	
	@commands.command(pass_context=True, aliases=[])
	async def veronica(self, context):
		"""mini Veronica"""
		await self.bot.send_file(context.message.channel, '{}VERONICA.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def stk9(self, context):
		"""Misteltein ???"""
		await self.bot.send_file(context.message.channel, '{}stk9.png'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def stk1(self, context):
		"""Seha and IPhone"""
		await self.bot.send_file(context.message.channel, '{}stk1.png'.format(self.base))
			
	@commands.command(pass_context=True, aliases=[])
	async def stk2(self, context):
		"""Seha sleep"""
		await self.bot.send_file(context.message.channel, '{}stk2.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk3(self, context):
		"""Seulbi love it"""
		await self.bot.send_file(context.message.channel, '{}stk3.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk4(self, context):
		"""Seubi what the hell I'm reading"""
		await self.bot.send_file(context.message.channel, '{}stk4.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk5(self, context):
		"""Yuri good"""
		await self.bot.send_file(context.message.channel, '{}stk5.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk6(self, context):
		"""Yuri sorry"""
		await self.bot.send_file(context.message.channel, '{}stk6.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk7(self, context):
		"""J hit"""
		await self.bot.send_file(context.message.channel, '{}stk7.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk8(self, context):
		"""J hahaha"""
		await self.bot.send_file(context.message.channel, '{}stk8.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk10(self, context):
		"""Misteltein guten tag"""
		await self.bot.send_file(context.message.channel, '{}stk10.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk11(self, context):
		"""Nata GRRRRRR"""
		await self.bot.send_file(context.message.channel, '{}stk11.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk12(self, context):
		"""Nata It's me"""
		await self.bot.send_file(context.message.channel, '{}stk12.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk13(self, context):
		"""Levia likes it"""
		await self.bot.send_file(context.message.channel, '{}stk13.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk14(self, context):
		"""Levia O_O"""
		await self.bot.send_file(context.message.channel, '{}stk14.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk15(self, context):
		"""Harpy love"""
		await self.bot.send_file(context.message.channel, '{}stk15.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk16(self, context):
		await self.bot.send_file(context.message.channel, '{}stk16.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk17(self, context):
		"""Tina mad mood"""
		await self.bot.send_file(context.message.channel, '{}stk17.png'.format(self.base))
					
	@commands.command(pass_context=True, aliases=[])
	async def stk18(self, context):
		await self.bot.send_file(context.message.channel, '{}stk18.png'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def camilla(self, context):
		await self.bot.send_file(context.message.channel, '{}CAMILLA.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def nata(self, context):
		"""mini Nata"""
		await self.bot.send_file(context.message.channel, '{}NATA.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def trainer(self, context):
		await self.bot.send_file(context.message.channel, '{}TRAINER.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def youjong(self, context):
		await self.bot.send_file(context.message.channel, '{}youjong.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def yuri(self, context):
		"""Mini Yuri"""
		await self.bot.send_file(context.message.channel, '{}petYURI.PNG'.format(self.base))
		
def setup(bot):
	n = closerspet(bot)
	bot.add_cog(n)
