import discord, json, requests, os
from discord.ext.commands import Bot
from discord import Intents
from random import randint, shuffle, choice

from src.core import *

with open('config.json') as fd:
    core.config = json.loads(fd.read())

root_dir = os.path.join('src', 'haikus')

client = Bot(
    command_prefix=core.config['prefix'],
    intents=Intents.all()
)

@client.event
async def on_ready():
    print('I am in the following guilds:')
    for guild in client.guilds:
        print(f'- {guild.name}')
    
    print(f'\nLogged in as "{client.user}" ({client.user.id})')

@client.command()
async def ping(ctx) -> None:
    """
    await ping()

    Ping pong!

    :param ctx object: Context
    :returns None: Nothing
    """

    await ctx.send('pong!')

@client.command()
async def addhaiku(
    ctx,
    name: str,
    *, lines: str
    ) -> None:
    """
    await addhaiku(name, lines)

    Creates a new haiku

    :param ctx object: Context
    :param name str: Name of the haiku
    :param lines str: Lines
    :returns None: Nothing
    """

    path = os.path.join(root_dir, name)

    if os.path.exists(path):
        return await ctx.send('Haiku already exists!')

    with open(f'{path}.txt', 'w+') as fd:
        fd.write(lines)

    await ctx.send('Added haiku')

@client.command()
async def haikus(ctx) -> None:
    """
    await ping()

    Lists all the haikus

    :param ctx object: Context
    :returns None: Nothing
    """

    haikus = []
    for _, _, files in os.walk(root_dir):
        for file in files:
            haikus.append(f'**-** {file.split(".")[0]}')

    await ctx.send("\n".join(haikus))

@client.command()
async def haiku(
    ctx,
    name: str | None = None
    ) -> None:
    """
    await haiku()

    Fetches a pre-made Haiku from the `src/haikus` folder

    :param ctx object: Context
    :param name str or None: Name of the haiku file, leave empty for random
    :returns None: Nothing
    """

    if name != None:
        path = os.path.join(root_dir, name) + '.txt'

        if not os.path.exists(path):
            return await ctx.send('Haiku not found!')
        
        haiku = path
    else:
        haikus = []
        for root, _, files in os.walk(root_dir):
            for file in files:
                haikus.append(os.path.join(root, file))
        
        haiku = choice(haikus)
    
    with open(haiku) as fd:
        haiku_lines = fd.read()

    await ctx.send(haiku_lines)

@client.command()
async def randhaiku(
    ctx, 
    keyword: str, 
    starts_with: str | None = None
    ) -> None:
    """
    await randhaiku(keyword, starts with)

    Generates a random haiku

    :param ctx object: Context
    :param starts_with str or None:
    :returns None: Nothing
    """

    url = f'https://haiku.kremer.dev/?keyword={keyword}'
    if starts_with != None:
        url += f'&starts_with={starts_with}'
    
    data = requests.get(url, headers={
        'User-Agent': 'Ryzhu 1.0'
    }).json()

    await ctx.send("\n".join(data))

if __name__ == '__main__':
    client.run(core.config['token'])