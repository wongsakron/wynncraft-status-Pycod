import discord
from discord.ext import commands
from discord.commands import slash_command,Option
import requests

class status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(guild_ids=[SEVER_ID],description='Show Status Player')
    async def status(
        self,
        ctx,
        name: Option(str, "Enter You Name"),
        chorice : Option(str, "T = Showdata", require=False,default='F')
    ):
        if chorice == 'T':
            chorice = False
        else :
            chorice = True
        try:
            print(name)
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
            embed.title = '🛰️〰️🔆〰️Welcome to Bot Status 〰️🔆〰️🚀'
            embed.add_field(name='🎎Name', value=f'`[{name1.capitalize()}]`', inline=True)
            embed.add_field(name='👑Rank', value=f'〰️`[{tag}]`', inline=True)
            try:    
                embed.add_field(name='🔰Guild', value=f'`[{guild[0].capitalize()}]` || `[{guild[1]}]`', inline=False)
            except:
                embed.add_field(name='🔰Guild', value=f'`[None]` || `[None]`', inline=False)
            embed.add_field(name='⚔️ Class', value=f'`[{classes[0].capitalize()}]`', inline=True)
            embed.add_field(name='🎯Level', value=f'〰️`[{classes[1]}]`', inline=True)
            embed.add_field(name='🗓️JoinDate', value=f'Frist : `[{firstjoin[:10]}]`', inline=False)
            embed.add_field(name='✈️Go To Web Site', value=f'{web}', inline=True)
        

            embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')

            embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'
        await ctx.respond(embed=embed,ephemeral=chorice)
        

    @commands.command()
    async def hello(self,ctx):
        await ctx.send('hihello')

def setup(bot):
    bot.add_cog(status(bot))
    print("Status on Ready")