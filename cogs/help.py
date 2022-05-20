import discord
from discord.ext import commands
from discord.commands import slash_command,Option

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(guild_ids=[SEVER_ID],description='Help Command')
    async def help(
        self,
        ctx,
        chorice : Option(str, "T = Showdata", require=False,default='F')
    ):
        if chorice == 'T':
            chorice = False
        else :
            chorice = True
        embed = discord.Embed(color=0xFFFF00 ,timestamp=discord.utils.utcnow())
        embed.title = 'Help'
        embed.description=f"""
        
        *** Use Command "/" ***
        
        ** Status Show data  : Status_Wyncraft

        ** How to Use : 
        `[/status name="Username" ||*chorice="T" (True) = Showdata, Default = false]`

        ** Wc Show data : Wc & Player Count

        ** How to Use : 
        `[/wc *chorice="T" (True) = Showdata , Default = false]`

        ***//..***
        """
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e6/Site-logo.png/revision/latest?cb=20210603200536')

        embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url='https://img.barks.jp/image/review/1000161129/01.jpg')
        await ctx.respond(embed=embed,ephemeral=chorice)
        
def setup(bot):
    bot.add_cog(Help(bot))
    print("help on Ready")