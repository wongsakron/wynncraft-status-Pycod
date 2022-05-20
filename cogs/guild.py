import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import requests

class Guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[SEVER_ID])
    async def guild(
        self,
        ctx,
        name : Option(str ,"name Guild ",require=False,default='LBL'),
        chorice : Option(str, 'T = Showdata', require=False,default='F')
    ):
        if chorice == 'T':
            chorice = False
        else :
            chorice = True
        try:
            embed = discord.Embed(color=0xF4BFBF, timestamp=discord.utils.utcnow())
            URl1 = "https://wynncraft.com/stats/guild/"
            URl2 = "https://api.wynncraft.com/public_api.php?action=guildStats&command="
            req = requests.get("https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe=alltime")
            i = req.json()
            x = i['data']
            Guildname = name

            
            for i in x:
                prefix = i['prefix']
            
                if Guildname == prefix:
                    name1 = i['name']
                    level = i['level']
                    created = i['created']
                    member = i['membersCount']
                    num = i['num']
                    try:
                        war = i['warCount']
                    except:
                        war = "None"
                    
                    req = requests.get(f'{URl2}{name1}')
                    r = req.json()
                    owner = r['members'][0]['name'] 
                    xp = r['xp']
                    URl = name1.split()
                    URl = '%20'.join(URl)
                    
                    embed.title ='🛰️〰️🔆〰️Welcome to Bot Status 〰️🔆〰️🚀'
                    embed.add_field(name='🔰Guild', value=f'`[{name1}]` || `[{prefix}]` ', inline=True)
                    embed.add_field(name='🏆 Top', value=f'〰️`[#{num}]`', inline=True)
                    embed.add_field(name='👑Guild Leader', value=f'`[{owner}] >> [Owner]`', inline=False)
                    embed.add_field(name='👨‍🚀Member', value=f'`[Total] >> [{member}]`', inline=True)
                    embed.add_field(name='🎯Level & Up', value=f' `[{level}] >> [{xp}%]`', inline=True)
                    embed.add_field(name='⚔️Guild War Atk', value=f'`[Total] >> [{war}]`', inline=False)
                    embed.add_field(name='🛠️Created', value=f'`[Data] >> [{created[:10]}]`', inline=False)
                    embed.add_field(name='✈️Go To Web Site', value=f'{URl1}{URl}', inline=False)
                    break
                
            embed.set_thumbnail(url=f'https://wynn-guild-banner.herokuapp.com/banners/{URl}')
            embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
                
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'
        await ctx.respond(embed=embed,ephemeral=chorice)

def setup(bot):
    bot.add_cog(Guild(bot))
    print("Guild on Ready")