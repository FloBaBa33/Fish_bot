import discord
import asyncio
import asyncpg
import datetime
from discord.ext import commands
from Fisch_cogs import json_auslese
intents = discord.Intents.all()
Class = json_auslese.Config()
cogs = ["Fisch_cogs.Admin", "Fisch_cogs.Commands", "Fisch_cogs.Events", "Fisch_cogs.Levels", "Fisch_cogs.test"]
# "Fisch_cogs.Voice" muss noch rein

bot = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True, help_command=None, intents=intents)
bot.remove_command("help")


async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database="lvlDB", user="postgres", password=Class.get_Password())


# todo rollenvergabe
#  kickfunktion mit abstimmung
#  twitch-Ankündigungen vorzug der community
#  Geburtstagsbot
#  Musikbot

@bot.event
async def on_ready():
    print("***********")
    print("loggt in as")
    print(bot.user.name)
    print("***********")
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except:
            pass
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nach dem Server"))
    channel = bot.get_channel(int(Class.get_Main()))
    date = datetime.datetime.now()
    await channel.send(f"Einen wunderschönen {date.day}.{date.month}!!!")


@bot.command()
async def test(ctx, arg=None):
    print(f"{ctx.author} + {arg}")
    pass


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"das Modul: {extension} wurde gestartet!")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"das Modul: {extension} wurde gestoppt!")


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await asyncio.sleep(5)
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"das Modul: {extension} wurde neu gestartet!")


@bot.event
async def on_message(message):
    if message.guild is None:
        print(f'--> "{message.author}" hat "{message.content}" geschrieben')
    else:
        print(f'--> "{message.author}" hat "{message.content}" auf dem Server "{message.guild}" in dem Channel {message.channel} geschrieben.')


bot.loop.run_until_complete(create_db_pool())
Token = Class.get_token()
bot.run(Token)
