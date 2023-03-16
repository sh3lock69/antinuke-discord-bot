import discord
from discord.ext import commands

Linkx= "https://discord.com/api/webhooks/1085899725867335720/utsCooFutggT2L0t-SXM64a9IGXV-QJVSUA8ffcVIwdq2pjUBKKT5rh07mVSTdaUhJly"


class Antihoist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if after.bot:
            return
        g = await self.client.get_guild_config(after.guild.id)
        if not g['antihoisting']:
            return

        
        


async def setup(client):
    await client.add_cog(Antihoist(client))