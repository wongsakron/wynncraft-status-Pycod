import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import requests
import os
from dotenv import load_dotenv
from cogs.fn.chorice import fncheck
from cogs.fn.API import data_wc

load_dotenv()
Sever = os.getenv("SEVER_ID")

class WC_example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[Sever])
    async def countwc(
        self,
        ctx,
        start: Option(int, 'Enter You start Wc >!Max 25 WC'),
        end: Option(int, 'Enter You End Wc  >!Max 25 WC'),
        chorice : Option(str, 'T = Showdata', require=False,default='F')
    ):
        
        try:
            chorice = fncheck(chorice)
            embed = discord.Embed(color=0xB983FF, timestamp=discord.utils.utcnow())
            embed.title = '🛰️〰️🔆〰️Welcome to Bot WcSever 〰️🔆〰️🚀'
            count,wc = data_wc(start,end)
            for i in range(len(count)):
                if count[i] >= 40 :
                    embed.add_field(name='❌', value=f'`[{wc[i]} == {count[i]}]`', inline=True)
                elif count[i] >= 30  :
                    embed.add_field(name='🔸', value=f'`[{wc[i]} == {count[i]}]`', inline=True)
                elif count[i] >= 20  :
                    embed.add_field(name='🔹', value=f'`[{wc[i]} == {count[i]}]`', inline=True)
                elif count[i] >= 10  :
                    embed.add_field(name='🟩', value=f'`[{wc[i]} == {count[i]}]`', inline=True)
                else:
                    embed.add_field(name='◽', value=f'`[{wc[i]} == {count[i]}]`', inline=True)

            embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')
            embed.set_footer(text='🛠️ Bot By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'
        await ctx.respond(embed=embed,ephemeral=chorice)

def setup(bot):
    bot.add_cog(WC_example(bot))