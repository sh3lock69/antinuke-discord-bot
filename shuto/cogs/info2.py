import discord
from discord.ext import commands
from utils.date import time
from utils.emojis import EMOJIS
import utils
from utils.shuto import bot_author_icon, Bot_name
import datetime


class UserinfoView(commands.Cog):

    def __init__(self, client):
        self.client = client

    @discord.ui.button(label="Info",style=discord.ButtonStyle.blurple, disabled=True)
    async def info(self, b: discord.ui.Button, interaction: discord.Interaction):
        self.susu(b)
        await interaction.message.edit(embed=self.embeds[0], view=self)

    @discord.ui.button(label="Roles", emoji='<:role:890807676697710622>', style=discord.ButtonStyle.blurple)
    async def roles(self, b: discord.ui.Button, interaction: discord.Interaction):
        self.susu(b)
        await interaction.message.edit(embed=self.embeds[1], view=self)

    @discord.ui.button(label="Permissions", emoji='🛠️', style=discord.ButtonStyle.blurple)
    async def permissions(self, b: discord.ui.Button, interaction: discord.Interaction):
        self.susu(b)
        await interaction.message.edit(embed=self.embeds[2], view=self)

    def susu(self, b):
        for i in self.children:
            i.disabled = False
        b.disabled = True


class info5(commands.Cog, description="Statistic related commands"):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(help="Get COVID-19 stats about any country.")
    async def covid(self, ctx, *, country=None):
        PREFIX = ctx.clean_prefix
        if country is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply("invalid usage!")

        try:
            async with self.client.session.get(f"https://coronavirus-19-api.herokuapp.com/countries/{country.lower()}") as r:
                response = await r.json()
        except Exception:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply("error")

        country = response['country']
        total_cases = response['cases']
        today_cases = response['todayCases']
        total_deaths = response['deaths']
        today_deaths = response['todayDeaths']
        recovered = response['recovered']
        active_cases = response['active']
        critical_cases = response['critical']
        total_tests = response['totalTests']
        cases_per_one_million = response['casesPerOneMillion']
        deaths_per_one_million = response['deathsPerOneMillion']
        tests_per_one_million = response['testsPerOneMillion']

        embed = discord.Embed(
            title=f"COVID-19 Status of {country}",
            description="This information isn't always live, so it may not be accurate."
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")

        embed.add_field(
            name="Total",
            value=f"""
```yaml
Total Cases: {total_cases}
Total Deaths: {total_deaths}
Total Tests: {total_tests}
```
            """,
            inline=False
        )
        embed.add_field(
            name="Today",
            value=f"""
```yaml
Today Cases: {today_cases}
Today Deaths: {today_deaths}
```
            """,
            inline=False
        )
        embed.add_field(
            name="Other",
            value=f"""
```yaml
Recovered: {recovered}
Active Cases: {active_cases}
Critical Cases: {critical_cases}
```
            """,
            inline=False
        )
        embed.add_field(
            name="Per One Million",
            value=f"""
```yaml
Cases Per One Million: {cases_per_one_million}
Deaths Per One Million: {deaths_per_one_million}
Tests Per One Million: {tests_per_one_million}
```
            """,
            inline=False
        )

        await ctx.message.reply(embed=embed)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(help="Get info about a role.")
    async def roleinfo(self, ctx: commands.Context, role: discord.Role = None):
        prefix = ctx.clean_prefix
        if role is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("invalid usage!")
        embed = discord.Embed(
            title=f"{EMOJIS['tick_yes']} Role Information",
            color=role.color
        )
        embed.add_field(
            name="Basic Info:",
            value=f"""
```yaml
Name: {role.name}
ID: {role.id}
Position: {role.position}
Color: {str(role.color)[1:]}
Hoisted: {role.hoist}
Members: {len(role.members)}
```
            """,
            inline=False
        )
        something = ""
        for permission in role.permissions:
            a, b = permission
            a = ' '.join(a.split('_')).title()
            hmm = '+' if b else '-'
            something += hmm + ' ' + a + '\n'
        embed.add_field(
            name="Permissions:",
            value=f"```diff\n{something}\n```",
            inline=False
        )
        await ctx.reply(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Get info about the server!")
    async def serverinfo(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild
        embed = discord.Embed(
            title="Server Information",
            description=f"Description: {guild.description}"
        ).set_author(
            name=guild.name,
            icon_url=guild.me.display_avatar.url if guild.icon is None else guild.icon.url
        ).set_footer(text=f"ID: {guild.id}")
        if guild.icon is not None:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(
            name="Basic Info:",
            value=f"""
**Owner:** <@{guild.owner_id}>
**Created At:** <t:round(time.time() - (guild.created_at) - time.time())):F>
**Region:** {str(guild.region).title()}
**System Channel:** {"None" if guild.system_channel is None else guild.system_channel.mention}
**Verification Level:** {str(guild.verification_level).title()}
            """,
            inline=False
        )
        embed.add_field(
            name="Members Info:",
            value=f"""
**Members:** `{len(guild.members)}`
**Humans:** `{len(list(filter(lambda m: not m.bot, guild.members)))}`
**Bots:** `{len(list(filter(lambda m: m.bot, guild.members)))}`
            """,
            inline=True
        )
        embed.add_field(
            name="Channels Info:",
            value=f"""
**Categories:** `{len(guild.categories)}`
**Text Channels:** `{len(guild.text_channels)}`
**Voice Channels:** `{len(guild.voice_channels)}`
**Threads:** `{len(guild.threads)}`
            """,
            inline=True
        )
        embed.add_field(
            name="Other Info:",
            value=f"""
**Roles:** `{len(guild.roles)}`
**Emojis:** `{len(guild.emojis)}`
**Stickers:** `{len(guild.stickers)}`
                """
        )
        if guild.features:
            embed.add_field(
                name="Features:",
                value=', '.join([feature.replace('_', ' ').title() for feature in guild.features]),
                inline=False
            )
        if guild.banner is not None:
            embed.set_image(url=guild.banner.url)

        return await ctx.reply(embed=embed)


    
#     @commands.cooldown(1, 60, commands.BucketType.user)
#     @commands.command(aliases=['stats'], help="Get info about me!")
#     async def botinfo(self, ctx):
#         msg = await ctx.message.reply(embed=discord.Embed(title=f"Loading... {EMOJIS['loading']}"))
#         embed = discord.Embed(
#             title="Information About Me!",
#             description="I am a simple, multipurpose Discord bot, built to make ur Discord life easier!",
#             color=MAIN_COLOR
#         ).set_thumbnail(url=self.client.user.display_avatar.url)
#         embed.add_field(
#             name="Stats",
#             value=f"""
# ```yaml
# Servers: {len(self.client.guilds)}
# Users: {len(set(self.client.get_all_members()))}
# Total Commands: {len(self.client.commands)}
# Uptime: {str(datetime.timedelta(seconds=int(round(time.time()-start_time))))}
# Version: V2 Rewrite
# ```
#             """,
#             inline=False
#         )
# #         async with self.client.session.get("https://statcord.com/logan/stats/751100444188737617") as r:
# #             ah_yes = await r.json()
# #         embed.add_field(
# #             name="Statcord Stats",
# #             value=f"""
# # ```yaml
# # Commands Ran Today: {ah_yes['data'][::-1][0]['commands']}
# # Most Used Command: {ah_yes['data'][::-1][0]['popular'][0]['name']} - {ah_yes['data'][::-1][0]['popular'][0]['count']} uses
# # Memory Usage: {'%.1f' % float(int(ah_yes['data'][::-1][0]['memactive'])/1000000000)} GB / {'%.1f' % float(int(psutil.virtual_memory().total)/1000000000)} GB
# # Memory Load: {ah_yes['data'][::-1][0]['memload']}%
# # CPU Load: {ah_yes['data'][::-1][0]['cpuload']}%
# # ```
# #             """,
# #             inline=False
# #         )
#         embed.add_field(
#             name="Links",
#             value=f"""
# - [Dashboard]({WEBSITE_LINK})
# - [Support Server]({SUPPORT_SERVER_LINK})
# - [Invite EpicBot]({INVITE_BOT_LINK})
# - [Vote EpicBot]({WEBSITE_LINK}/vote)
#             """,
#             inline=True
#         )
#         embed.add_field(
#             name="Owner Info",
#             value="""
# Made by: **[Nirlep\_5252\_](https://discord.com/users/558861606063308822)**
#             """,
#             inline=True
#         )

#         await msg.edit(embed=embed)

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(aliases=['stats'], help="Get info about me!")
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Info about me!",
            description="A simple multipurpose Discord bot.",
            timestamp=datetime.datetime.utcnow()
        ).add_field(
            name="Stats:",
            value=f"""
**Servers:** {len(self.client.guilds)}
**Users:** {len(self.client.users)}
**Commands:** {len(self.client.commands)}
**Uptime:** {str(datetime.timedelta(seconds=int(round())))}
**Version:** V2 Rewrite
            """,
            inline=True
        ).add_field(
            name="Links:",
            value=f"""
- [Website]()
- [Support]()
- [Invite]()
- [Vote](/vote)
- [Github](https://github.com/nirlep5252/epicbot)
            """,
            inline=True
        ).set_footer(text=self.client.user.name, icon_url=self.client.user.display_avatar.url
        ).set_author(name=self.client.user.name, icon_url=self.client.user.display_avatar.url
        ).set_thumbnail(url=self.client.user.display_avatar.url)
        try:
            embed.add_field(
                name="Latest Commits:",
                inline=False
            )
        except Exception:
            pass
        await ctx.reply(embed=embed)
Linkx= "https://discord.com/api/webhooks/1085899725867335720/utsCooFutggT2L0t-SXM64a9IGXV-QJVSUA8ffcVIwdq2pjUBKKT5rh07mVSTdaUhJly"

async def setup(client):
    await client.add_cog(info5(client))
