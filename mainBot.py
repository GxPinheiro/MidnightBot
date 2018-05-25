import discord
from discord.ext import commands
import plugins

description = '''MidnightBot Several uses for no reason'''
bot = commands.Bot(command_prefix='!!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



# @bot.command()
# async def roll(dice : str):
#     """Rolls a dice in NdN format."""
#     try:
#         rolls, limit = map(int, dice.split('d'))
#     except Exception:
#         await bot.say('Format has to be in NdN!')
#         return

#     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#     await bot.say(result)

@bot.command(description='Help you to decide your life')
async def choose(*choices : str):
    """Decide your life"""
    await bot.say(random.choice(choices))


@bot.command()
async def joined(member : discord.Member):
    """Alerts when a member enter the server"""
    await bot.say('{0.name} invaded {0.joined_at}'.format(member))

# @bot.command()
# async def music(*)

@bot.command()
async def funcname(phrase : str):
    echo.print

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')



bot.run('NDQ4NjMzMjQxMzk0NzQxMjQ4.DeY_ow.SktFlzgpKzyMXTo4a0l5XfAa6QA')
