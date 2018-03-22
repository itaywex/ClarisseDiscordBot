import discord
import asyncio
import random


presence_list = ['Watching over Ryouko', 'Fighting the squids', 'Managing fan clubs', 'Reading CQ', "Stalking Hiero"]
presence_change_delay_seconds = 30 * 60

async def periodic_change(bot):
    while True:
        new_presence = random.choice(presence_list)
        print(f'Changing presence to {new_presence}')
        await bot.change_presence(game=discord.Game(name=new_presence))
        await asyncio.sleep(presence_change_delay_seconds)


async def start_presence_change(bot):
    loop = asyncio.get_event_loop()
    loop.create_task(periodic_change(bot))


