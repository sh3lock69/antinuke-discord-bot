import asyncio
import validators
import discord
from discord.ext import commands
from cogs.mod import commands
import datetime


from discord import Embed
time = datetime.datetime.utcnow()

def success_embed(title, description, timestamp):
    return Embed(
        title=title,
        description=description,
        timestamp=time
        
        
    )

def error_embed(title, description):
    return Embed(
        title=title,
        description=description,
        timestamp=time
        
        
    )

error_embed_2 = discord.Embed(
    title="error",
    description=f"you dont have perms {commands.__name__}"
    )