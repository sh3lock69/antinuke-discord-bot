import discord
from discord.ext import commands

from config import ANTIHOIST_CHARS


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

        if after.display_name[0] in ANTIHOIST_CHARS and not after.display_name.startswith("[AFK] "):
            try:
                await after.edit(
                    nick=before.display_name if before.display_name[0] not in ANTIHOIST_CHARS else "Moderated Nickname",
                    reason="EpicBot Antihoisting"
                )
            except Exception:
                pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            return
        g = await self.client.get_guild_config(member.guild.id)
        if not g['antihoisting']:
            return

        if member.display_name[0] in ANTIHOIST_CHARS:
            try:
                await member.edit(
                    nick="Moderated Nickname",
                    reason="EpicBot Antihoisting"
                )
            except Exception:
                pass


async def setup(client):
    await client.add_cog(Antihoist(client))