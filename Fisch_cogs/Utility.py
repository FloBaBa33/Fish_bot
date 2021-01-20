import discord
from discord.ext import commands
from cogs import json_auslese
Class = json_auslese.Config()

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["arzt"])
    async def doc(self, ctx, arg=discord.member):