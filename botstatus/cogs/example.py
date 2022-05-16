from email.policy import default
from secrets import choice
from typing_extensions import Required
import discord
from discord.ext import commands
from discord.commands import slash_command,Option
from pkg_resources import require
import requests
from sqlalchemy import false, true

class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(guild_ids=[SEVER_ID])
    async def status(
        self,
        ctx,
        name: Option(str, 'Enter You Name'),
        chorice : Option(str, 'T = Showdata', require=False,default='F')
    ):
        if chorice == 'T':
            chorice = False
        else :
            chorice = True
        web = f'https://wynncraft.com/stats/player/{name}'
        URl = f'https://api.wynncraft.com/v2/player/{name}/stats'
        req = requests.get(URl)
        i = req.json()
        status = i['data'][0]
        classes = status['classes'][0]
        name1 = status['username']
        firstjoin = status['meta']['firstJoin']
        classes = (classes['name'], classes['level'])
        x = status['guild']
        guild = (x['name'], x['rank'])
        tag = status['meta']['tag']['value']
        embed = discord.Embed(color=0xCC33FF ,timestamp=discord.utils.utcnow())
        embed.title = '///Status_Player///'
        embed.description = 'Wynncraft Sever'
        embed.add_field(name='Name', value=f'{name1.capitalize()}', inline=True)
        embed.add_field(name='Rank', value=f'{tag}', inline=True)
        embed.add_field(name='Guild', value=f'{guild[0].capitalize()}', inline=False)
        embed.add_field(name='Rank', value=f'{guild[1].capitalize()}', inline=False)
        embed.add_field(name='Class', value=f'{classes[0].capitalize()}', inline=True)
        embed.add_field(name='Level', value=f'{classes[1]}', inline=True)
        embed.add_field(name='JoinTime', value=f'Frist : {firstjoin[:10]} Date', inline=False)
        embed.add_field(name='Go To Web Site', value=f'{web}', inline=True)
        

        embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')

        embed.set_footer(text='Bot By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        await ctx.respond(embed=embed,ephemeral=chorice)

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('hihello')

def setup(bot):
    bot.add_cog(example(bot))
