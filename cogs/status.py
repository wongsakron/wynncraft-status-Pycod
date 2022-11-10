import discord
from discord.ext import commands
from discord.commands import slash_command,Option
import os
from dotenv import load_dotenv
from cogs.fn.API import data_player
from cogs.fn.chorice import fncheck

load_dotenv()
Sever = os.getenv("SEVER_ID")

class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(guild_ids=[Sever])
    async def status(
            self,
            ctx,
            name: Option(str, 'Enter You Name'),
            chorice : Option(str, 'T = Showdata', require=False,default='F')
    ):
        try:
            chorice = fncheck(chorice)  
            WYN = data_player(name)
            embed = discord.Embed(color=0xCC33FF ,timestamp=discord.utils.utcnow())
            embed.title = '🛰️〰️🔆〰️Welcome to Bot Status 〰️🔆〰️🚀'
            embed.add_field(name='🎎Name', value=f'`[{WYN["name"]}]`', inline=True)
            embed.add_field(name='👑Rank', value=f'〰️`[{WYN["tag"]}]`', inline=True)
            embed.add_field(name='🔰Guild', value=f'`[{WYN["guild"]}]` || `[{WYN["rank"]}]`', inline=False)
            embed.add_field(name='⚔️ Class', value=f'`[{WYN["class"]}]`', inline=True)
            embed.add_field(name='🎯Level', value=f'〰️`[{WYN["level"]}]`', inline=True)
            embed.add_field(name='🗓️JoinDate', value=f'Frist : `[{WYN["first"]}]`', inline=False)
            embed.add_field(name='✈️Go To Web Site', value=f'{WYN["web"]}', inline=True)
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')
            embed.set_footer(text='🛠️ Bot By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'
        await ctx.respond(embed=embed,ephemeral=chorice)
        


def setup(bot):
    bot.add_cog(example(bot))