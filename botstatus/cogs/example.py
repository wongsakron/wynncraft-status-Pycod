import discord
from discord.ext import commands
from discord.commands import slash_command,Option
import requests
from sqlalchemy import false, true

class example(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(guild_ids=[DISCORD_ID])
    async def status(
        self,
        ctx,
        name1: Option(str, 'Enter You Name')
    ):
        req = requests.get(f"https://api.wynncraft.com/v2/player/{name1}/stats")
        i = req.json()
        status = i['data'][0]
        classes = status['classes'][0]
        name = status['username']
        firstjoin = status['meta']['firstJoin']
        classes = (classes['name'], classes['level'])
        x = status['guild']
        guild = (x['name'], x['rank'])
        tag = status['meta']['tag']['value']
        embed = discord.Embed(color=0xCC33FF ,timestamp=discord.utils.utcnow())
        embed.title = '///Status_Player///'
        embed.description = 'Wynncraft Sever'
        embed.add_field(name='Name', value=f'{name}', inline=True)
        embed.add_field(name='Rank', value=f'{tag}', inline=True)
        embed.add_field(name='Class', value=f'{classes[0]}', inline=False)
        embed.add_field(name='Level', value=f'{classes[1]}', inline=True)
        embed.add_field(name='Guild', value=f'{guild[0]}', inline=False)
        embed.add_field(name='Rank', value=f'{guild[1]}', inline=False)

        embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')

        embed.set_footer(text='Bot By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')

        await ctx.respond(embed=embed,ephemeral=True)

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('hihello')

def setup(bot):
    bot.add_cog(example(bot))