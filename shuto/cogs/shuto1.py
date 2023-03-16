import discord
from discord.ext import commands




class Antihois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if after.bot:
            return
     

async def setup(client):
    await client.add_cog(Antihois(client))