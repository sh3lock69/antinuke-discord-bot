import discord

from discord.ext import commands
from discord.utils import escape_markdown









class nsfw(commands.Cog, description="Oh boi..."):
    def __init__(self, client):
        self.client = client

    async def get_image_from_api(self, url, thing):
        async with self.client.session.get(url) as r:
            uwu = await r.json()
            image = uwu[thing]
            return discord.Embed().set_image(url=image)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Fuck someone!")
    async def fuck(self, ctx: commands.Context, user: discord.Member = None):
        if user is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        embed = await self.get_image_from_api("https://purrbot.site/api/img/nsfw/fuck/gif", "link")
        embed.title = "Wowie!"
        embed.description = f"**{escape_markdown(str(user.name))}** got fucked hard by **{escape_markdown(str(ctx.author.name))}**"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Cum inside someone ><")
    async def cum(self, ctx: commands.Context, user: discord.Member = None):
        if user is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        embed = await self.get_image_from_api("https://purrbot.site/api/img/nsfw/cum/gif", "link")
        embed.title = f"Mmmm"
        embed.description = f"**{escape_markdown(str(ctx.author.name))}** cummed inside **{escape_markdown(str(user.name))}**"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Someones being naughty? Spank them!")
    async def spank(self, ctx: commands.Context, user: discord.Member = None):
        if user is None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user == ctx.author:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        if user.bot:
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply("error")
        embed = await self.get_image_from_api("https://nekos.life/api/v2/img/spank", "url")
        embed.title = "Damn!"
        embed.description = f"**{escape_markdown(str(ctx.author.name))}** spanked **{escape_markdown(str(user.name))}**"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Hentai...")
    async def hentai(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://shiro.gg/api/images/nsfw/hentai", "url")
        embed.title = "There you go!"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Thighs...")
    async def thighs(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://shiro.gg/api/images/nsfw/thighs", "url")
        embed.title = "Yummy!!"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Nekos but NSFW gifs...")
    async def nekogif(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://purrbot.site/api/img/nsfw/neko/gif", "link")
        embed.title = "Gifs!"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Boobs...")
    async def boobs(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://nekos.life/api/v2/img/boobs", "url")
        embed.title = "Boooooobs! :D"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Blowjob...")
    async def blowjob(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://purrbot.site/api/img/nsfw/blowjob/gif", "link")
        embed.title = "Yummy! 😋"
        await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.is_nsfw()
    @commands.command(help="Pussies...")
    async def pussy(self, ctx: commands.Context):
        embed = await self.get_image_from_api("https://nekos.life/api/v2/img/pussy", "url")
        embed.title = "Yummy! 😋"
        await ctx.send(embed=embed)



async def setup(client):
    await client.add_cog(nsfw(client))
