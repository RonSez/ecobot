import discord
from discord.ext import commands
from botoken import bot_token
from func import get_random_air_pollution_fact, air_pollution_intro, get_random_solution

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.command()
async def intro(ctx):
    await ctx.send(f'Here is an introduction to air pollution: {air_pollution_intro()}')



@bot.command()
async def fact(ctx):
    await ctx.send(f'Here is a random air pollution fact: {get_random_air_pollution_fact()}')



@bot.command()
async def solution(ctx):
    await ctx.send(f'Here is a random air pollution solution: {get_random_solution()}')


@bot.command()
async def usage(ctx):
    """Displays information about each command."""
    help_text = """
    **Commands List:**
    $solution - Provides a random solution to air pollution.
    $fact - Provides a random air pollution fact.
    $intro - Introduces air pollution and its effects.
    """
    await ctx.send(help_text)


bot.run(bot_token)


