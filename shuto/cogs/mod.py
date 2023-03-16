import discord
from discord.ext import commands

from utils.embes import success_embed, error_embed
from utils.emojis import EMOJIS
import datetime
from utils.errors import missing_perms
time = datetime.datetime.utcnow()
import json
mention_member_error = f"```toml\n[]Invalid usage, Please mention a member <mention>```"
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'cogs synced suscesfuly')

    @commands.command()
    async def test(self, ctx):
        
        await ctx.send(embed=success_embed("error", "cool"))
    @commands.command(name="kick", aliases=["k", "ghumkea"], help="This cmd is used to kick someone from your server")
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *,reason = None):
        tittle = "error"
        author = ctx.author.display_avatar
        footer = time
        

        if member is None:
            await ctx.send()
        if member == ctx.author:
            
            await ctx.send(embed=error_embed(f'error',f"{EMOJIS['tick_no']} | You can not kick yourself {ctx.author.mention}"))
            return
        if member == self.client:
            await ctx.send(embed= error_embed(f"error", f"{EMOJIS['tick_no']} | You can not kick me, Dumbo!"))   
            return         
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="",
                description=f"{EMOJIS['tick_yes']} | Sucessfully kicked {member.mention}",
                timestamp=time,
            )
            embed.set_author(name=ctx.author.display_name, icon_url=author)
            await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(mention_member_error)
            
        else:
            await ctx.send(missing_perms)
    
    @commands.command(name="ban", aliases=["b"], help="This cmd is used to ban someone from your server")
    @commands.has_guild_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *,reason = None):
        tittle = "error"
        author = ctx.author.display_avatar
        footer = time
        

        if member is None:
            await ctx.send()
        if member == ctx.author:
            
            await ctx.send(embed=error_embed(f'error',f"{EMOJIS['tick_no']} | You can not ban yourself {ctx.author.mention}"))
            return
        if member == self.client:
            await ctx.send(embed= error_embed(f"error", f"{EMOJIS['tick_no']} | You can not ban me, Dumbo!"))   
            return         
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="",
                description=f"{EMOJIS['tick_yes']} | Sucessfully banned {member.mention}",
                timestamp=time,
            )
            embed.set_author(name=ctx.author.display_name, icon_url=author)
            await ctx.send(embed=embed)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(mention_member_error)
            
        else:
            await ctx.send(missing_perms)
    
    @commands.command(name="warn", 
                      help="warns a member in your server",
                       aliases=['w']
                       )
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.Member, *, reason=str):
        if reason == None:
            await ctx.send("please provide reason")
            return
        else:
            await ctx.send(f"{member.mention}has been warned for:{reason}")
    
        
            
    
        
        

async def setup(client):
    await client.add_cog(Moderation(client))