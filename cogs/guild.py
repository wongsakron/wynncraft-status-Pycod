import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import requests
import os
from dotenv import load_dotenv
from cogs.fn.chorice import fncheck
from cogs.fn.API import data_guilde

load_dotenv()
Sever = os.getenv("SEVER_ID")

class Guilde(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[Sever])
    async def guilde(
        self,
        ctx,
        name : Option(str ,"name Guild ",require=False,default='LBL'),
        chorice : Option(str, 'T = Showdata', require=False,default='F')
    ):
        try:
            chorice = fncheck(chorice)
            GUILD = data_guilde(name)

            embed = discord.Embed(color=0xF4BFBF, timestamp=discord.utils.utcnow())
            embed.title ='🛰️〰️🔆〰️Welcome to Bot Status 〰️🔆〰️🚀'
            embed.add_field(name='🔰Guild', value=f'`[{GUILD["name"]}]` || `[{GUILD["prefix"]}]`', inline=True)
            embed.add_field(name='🎯Level', value=f'〰️`[{GUILD["level"]}]`', inline=True)
            embed.add_field(name='👑Guild Leader', value=f'`[{GUILD["owner"]}] >> [Owner]`', inline=False)
            embed.add_field(name='👨‍🚀Member', value=f'`[Total] >> [{GUILD["member"]}]`', inline=True)
            embed.add_field(name='⚔️Guild War Atk', value=f'`[Total] >> [{GUILD["war"]}]`', inline=True)
            embed.add_field(name='🛠️Created', value=f'`[Data] >> [{GUILD["created"]}]`', inline=False)
            embed.add_field(name='✈️Go To Web Site', value=f'{GUILD["url"]}', inline=False)
            embed.set_thumbnail(url=f'{GUILD["banners"]}')
            embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
                
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'
        await ctx.respond(embed=embed,ephemeral=chorice)

def setup(bot):
    bot.add_cog(Guilde(bot))