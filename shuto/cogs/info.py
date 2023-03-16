import discord
from discord.ext import commands
from utils.date import time
from utils.emojis import EMOJIS
import utils
from utils.shuto import bot_author_icon, Bot_name


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Misc cog loaded\n-----')


    @commands.command()
    async def ping(self, ctx):
        latency = round(self.client.latency * 100)
        author_name = ctx.author.display_name
        author_icon = f"{bot_author_icon}"
        timestamp = time
        footer = f"Requested by: {ctx.author.display_name}"
        thumbnail = ctx.author.display_avatar

        ping_embed = discord.Embed(title=f"Ping",
                                   description=f"{EMOJIS['blue_arrow']} {latency}",
                                   timestamp=timestamp)
        ping_embed.set_author(name=f'{Bot_name}', icon_url=author_icon)
        ping_embed.set_footer(text=footer)
        ping_embed.set_thumbnail(url=thumbnail)
        await ctx.send(embed = ping_embed)

    @commands.command()
    async def avatar(self, ctx,  member : discord.Member=None):
        
        latency = round(self.client.latency * 100)
        author_name = ctx.author.display_name
        author_icon = f"{bot_author_icon}"
        timestamp = time
        footer = f"Requested by: {ctx.author.display_name}"
        thumbnail = ctx.author.display_avatar

        ping_embed = discord.Embed(title=f"",
                                   description=f"",
                                   timestamp=timestamp)
        ping_embed.set_author(name=author_name, icon_url=ctx.author.display_avatar)
        ping_embed.set_footer(text=footer)
        
        ping_embed.set_image(url=member.display_avatar)
        await ctx.send(embed = ping_embed)

    @commands.command()
    async def banner(self, ctx,  member : discord.Member=None):
        
        latency = round(self.client.latency * 100)
        author_name = ctx.author.display_name
        author_icon = f"{bot_author_icon}"
        timestamp = time
        footer = f"Requested by: {ctx.author.display_name}"
        thumbnail = ctx.author.display_avatar

        ping_embed = discord.Embed(title=f"",
                                   description=f"",
                                   timestamp=timestamp)
        ping_embed.set_author(name=author_name, icon_url=ctx.author.display_avatar)
        ping_embed.set_footer(text=footer)
        
        ping_embed.set_image(url=member.banner)
        await ctx.send(embed = ping_embed)




    

    
        
        

        

async def setup(client):
    await client.add_cog(info(client))
