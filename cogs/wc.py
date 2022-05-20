import discord
from discord.ext import commands
from discord.commands import slash_command, Option , permissions
import requests

class WCsever(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[SEVER_ID],description='Show Wc And Player Count')
    async def wc(
        self,
        ctx,
        chorice : Option(str, "T = Showdata", require=False,default='F')
    ):
        if chorice == 'T':
            chorice = False
        else :
            chorice = True
        embed = discord.Embed(color=0xCCFFFF, timestamp=discord.utils.utcnow())
        embed.title = '❀⊱┄┄┄┄┄┄┄ Wc_Sever ┄┄┄┄┄┄┄⊰❀'
        req = requests.get('https://api.wynncraft.com/public_api.php?action=onlinePlayers')
        i = req.json()
        x = []
        for key, value in i.items() :
             if key != 'request':
                 if key != 'YT':
                     a = (len(value))
                     if a >= 40:
                         x.extend([f'FU{key} = {a}'])
                     elif a >= 30:
                         x.extend([f'CO{key} = {a}'])
                     elif a >= 20:
                         x.extend([f'SO{key} = {a}'])
                     elif a >= 10:
                         x.extend([f'BL{key} = {a}'])
                     else:
                         x.extend([f'{key} = {a}'])
        for i in x:
                if i.startswith('FU') == True :
                    embed.add_field(name='❌', value=f'`[{i[2:]}]`', inline=True)
                elif i.startswith('CO') == True :
                    embed.add_field(name='🔸', value=f'`[{i[2:]}]`', inline=True)
                elif i.startswith('SO') == True :
                    embed.add_field(name='🔹', value=f'`[{i[2:]}]`', inline=True)
                elif i.startswith('BL') == True :
                    embed.add_field(name='🟩', value=f'`[{i[2:]}]`', inline=True)
                else:
                    embed.add_field(name='◽', value=f'`[{i}]`', inline=True)

        embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        await ctx.respond(embed=embed,ephemeral=chorice)

def setup(bot):
    bot.add_cog(WCsever(bot))
    print("Wc on Ready")