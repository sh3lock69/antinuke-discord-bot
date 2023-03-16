import discord
from discord.ext import commands
from config import Prefix

client = commands.Bot(
    command_prefix=Prefix,
    intents=discord.Intents.all()
)

Website = "https://drive.google.com/uc?export=download&id=17gjIvSnDfBZd7Y6T3Dlg_Y3Y1x9JNpSe"