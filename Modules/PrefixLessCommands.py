# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.

import discord
from discord.ext import commands


async def handle_prefixless_messages(bot, message):
    message_content = message.content.lower()

    if message_content.startswith('ryouko'):
        await bot.send_message(message.channel, "Best girl?")

    if message_content.startswith('mew'):
        await bot.send_message(message.channel, ":cat:")