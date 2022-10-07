import discord, json, requests
from discord.ext.commands import Bot
from discord import Intents
from random import randint, shuffle, choice

from src.core import *

with open('config.json') as fd:
    core.config = json.loads(fd.read())


client = Bot(
    command_prefix=core.config['prefix'],
    intents=Intents.all()
)

insults = [
    'fatass',
    'bald motherfucker',
    'fried chicken addict',
    'crackhead',
    'cunt',
    'idiot',
    'fatso',
    'bald ass mf',
    'skin tone chickenbone',
    'bitch',
    'fuck you',
    'fat ass bitch',
    'retard',
    'nerd',
    ':nerd:',
    'rat looking mf',
    'motherfucker',
    'asshole',
    'tiny cock',
    'tiny weenie',
    'shrimp dick'
]

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
async def catfact(ctx) -> None:
    """
    await catfact(context) -> nothing

    Sends a random fact about cats

    :param ctx object: Context
    :returns None: Nothing
    """
    
    req = requests.get('https://majoexe.xyz/api/v1/fun/cat_fact')
    data = json.loads(req.text)

    await ctx.send(f'**{data["cat_fact"]}**')

@client.command()
async def socialcredits(ctx, *, user: discord.User) -> None:
    """
    await socialcredits(context, user) -> nothing

    Calculates the given users social credits

    :param ctx object: Context
    :param user discord.User: The target user
    :returns None: Nothing
    """
    
    socialcredits = randint(
        -5000000, 
        +100000000
    )

    await ctx.send(f'{user.mention}, your social credit score is {str(socialcredits)}',)

@client.command()
async def insult(ctx, *, user: discord.User) -> None:
    """
    await insult(context, user) -> nothing

    Insults the target user

    :param ctx object: Context
    :param user discorc.User: The target user
    :returns None: Nothing
    """
    
    shuffle(insults)
    await ctx.send(f'{user.mention}, {choice(insults)}')

if __name__ == '__main__':
    client.run(core.config['token'])