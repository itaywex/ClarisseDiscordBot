# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
    
import discord
from discord.ext import commands

class BasicCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, *ctx):
        print("Test running")
        print(ctx)
        print (self)
        print (self.bot)
        await self.bot.say("Test successful")

    @commands.group(pass_context=True)
    async def cool(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await self.bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

    @cool.command(name='bot')
    async def _bot(self):
        """Is the bot cool?"""
        await self.bot.say('Yes, the bot is cool.')



def setup(bot):
    bot.add_cog(BasicCommands(bot))