# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import PrefixLessCommands as PLC
from Periodic import ChangePresence

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
clarisse = Bot(description="TTS inspired bot by Itaywex#0001", command_prefix=".", pm_help=False)


startup_extensions = ["Modules.BasicCommands"]

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@clarisse.event
async def on_ready():
    print('Logged in as '+clarisse.user.name+' (ID:'+clarisse.user.id+') | Connected to '+str(len(clarisse.servers))+' servers | Connected to '+str(len(set(clarisse.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(clarisse.user.name))
    print('https://discordapp.com/oauth2/authorize?clarisse_id={}&scope=bot&permissions=8'.format(clarisse.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Original bot Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('You are running Clarisse v2.1') 
    print('Created by Itaywex#0001') 
    print('\nBig thanks to Habchy#1665 for helping me set up the bot ')
    #ChangePresence.start_presence_change(clarisse)
    #loop.call_later(5, ChangePresence.start_presence_change, clarisse)

    await ChangePresence.start_presence_change(clarisse)

@clarisse.event
async def on_message(message):

    if message.author == clarisse.user:
        return

    await PLC.handle_prefixless_messages(clarisse, message)

    # This will enable other commands to run
    await clarisse.process_commands(message)


# This is a basic example of a call and response command. You tell it do "this" and it does it.
@clarisse.command()
async def dance(*args):

    await asyncio.sleep(0.2)
    await clarisse.say("\\o\\")
    await asyncio.sleep(0.3)
    await clarisse.say("/o/")
    await asyncio.sleep(0.3)
    await clarisse.say("\\o/")

# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.



if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            clarisse.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    clarisse.run('NDI2MDQ3ODk3ODUxNzg5MzEz.DZQTkg.a8jI98DgJCapxWa9BW8fPZBnXq4')

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.

# Big thanks to Habchy#1665 for his git rpository that helped me start with the bot 
# Check it out in https://github.com/Habchy/BasicBot

