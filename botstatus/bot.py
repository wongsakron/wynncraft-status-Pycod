import discord
import os
import json
from discord.ext import commands


with open('config/config.json') as config:
    data = json.load(config)

class stacia_bot(commands.Bot):
    def __init__(self,*args,**kwargs):
        self.token = data["token"]
        super().__init__(command_prefix=data["prefix"],*args,**kwargs)

bot = stacia_bot(owner_id=OWNER_id, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is Ready')

if __name__ == "__main__":
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    bot.run(bot.token)