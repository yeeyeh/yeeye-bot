import discord
from discord import channel
from discord import Game
from discord.ext.commands import Bot
import random
import requests
import asyncio
import json



BOT_PREFIX = 'y!'
TOKEN = 'NDc1MTEyODUzNDEwNTQ1Njc1.DqgiMA.NOjB5eX1XqJs7PCgRPjG3AL6BV8'

def get_channel(channels, channel_name):
    for channel in client.get_all_channels():
        print(channel)
        if channel.name == channel_name:
            return channel
    return None

client = Bot(command_prefix=BOT_PREFIX)


#Passive-Aggressive 8ball
@client.command(name='8ball',
                description="Passive-Aggressively answers your questions.",
                brief="Answers questions.",
                aliases =['eightball', 'eight_ball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Yes',
        'No',
        'Maybe',
        'Hell no',
        'Fuck off',
        'If you really want it to, sure',
        'I guess',
        'I don\'t even know',
        'I thought you already knew the answer',
        'Whatever',
        'Sure',
        'Uh, no',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='fortune',
                description="Advanced wisdom brought to you by baked goods.",
                brief="Food gives you fortune.",
                aliases =['cookie', 'fortune_cookie'],
                pass_context=True)
async def fortune(context):
    possible_responses = [
        ' Know a person with time; know a horse with distance.',
        ' People try thing, because they just don\'t want it enough.',
        ' Behind an able man. There are always.',
        ' Discriminating mind leads you in the proper direction.',
        ' Help! I\'m stuck in a digital fortune cookie factory!',
        ' Would you like to do someone a favor?',
        ' :) We are very happy together :)',
        ' Fortune Not Found.',
        ' You are not illiterate.',
        ' If the brain were so simple we could understand it, we would be so simple we could\'nt.',
        ' Special touches have been planned with you in mind.',
        ' Don\'t panic.',
        ' Only listen to this bot, disregard all other fortune telling units.',
        ' To truly find yourself, you must play hide and seek alone.'
    ]
    await client.say(context.message.author.mention + " " + random.choice(possible_responses))


#square a number
@client.command()
async def square(number: int):
    squared = number * number
    await client.say(str(number) + " squared is " + str(squared))


@client.command(name='tits',
                description="Tits!",
                brief="Tits!",)
async def tits():
    await client.say('( . Y . )')


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value= response.json()['bpi']['USD']['rate']
    await client.say("Right now, a bitcoin costs: $" + value)


#@client.command()
#async def mute():


#idiot detector
@client.event

async def on_message(message):

    #check for xd
    if "xd" in message.content:
            await client.send_message(message.channel, 'ecks dee in <current year> what a nerd')
    if "xD" in message.content:
            await client.send_message(message.channel, 'ecks dee in <current year> what a nerd')
    if "Xd" in message.content:
            await client.send_message(message.channel, 'ecks dee in <current year> what a nerd')
    if "XD" in message.content:
            await client.send_message(message.channel, 'ecks dee in <current year> what a nerd')

    #check for furries
    if "OWO" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "OwO" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "owo" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "Owo" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "owO" in message.content:
           await client.send_message(message.channel, 'get out of here furry')

    if "UWU" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "UwU" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "uwu" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "Uwu" in message.content:
           await client.send_message(message.channel, 'get out of here furry')
    if "uwU" in message.content:
           await client.send_message(message.channel, 'get out of here furry')



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="i am a shit bot"))
    print('Logged in as ' + client.user.name)
    print('ID: ' + client.user.id)
    print('----------')


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print('----------')
        print("Current servers: " + str(len(client.servers)))
        print('----------')
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)


#ACTIVATE HACKS