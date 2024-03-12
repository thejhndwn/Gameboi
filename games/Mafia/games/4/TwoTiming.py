import discord
from discord.ext import commands


class TwoTiming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx, member: discord.Member):
        pass

    @commands.command()
    async def help(self):
        pass

    @commands.command()
    async def player(self):
        pass

    @commands.command() #pass the args
    async def useItem(self):
        pass

    @commands.command()
    async def giveItem(self):
        pass