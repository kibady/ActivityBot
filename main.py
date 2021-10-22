import json
import requests
from discord_components import DiscordComponents, Button, ButtonStyle
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 

async def change_status():
    await bot.wait_until_ready()
    while not bot.is_closed():
        await bot.change_presence(activity = discord.Game(name=f"Бот находится на {len(bot.guilds)} серверах"))
        await asyncio.sleep(4)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "!help"))
        await asyncio.sleep(3)

@bot.remove_command('help')

@bot.event
async def on_ready():
    print("ActivityBot has been started. Developer: STROITEL#7181")
    print("[!] Status: OK") 

@bot.command()
async def invite(ctx):
        embed = discord.Embed( title="**Кликните чтобы добавить данного бота на сервер**", url="https://discord.com/oauth2/authorize?client_id=890942267676848168&scope=bot+applications.commands", colour = 3092790)
        embed.set_author(name="឵",url="https://s9.gifyu.com/images/PRIGLASENIE.gif")
        await ctx.channel.send(embed = embed)

@bot.command()
async def youtube(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 880218394199220334,  # Youtube Together
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к просмотру «YouTube Together»", url = f"https://discord.com/invite/{link['code']}", reference=ctx.message.to_reference(), colour = discord.Colour.from_rgb(255, 0, 0)))
 
@bot.command()
async def poker(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 755827207812677713,  # Poker Night
        "target_type": 2,
        "temporary": False,
        "validate": None

    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Poker Night»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(255, 255, 255)))

@bot.command()
async def fish(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 814288819477020702,  # Fishington
        "target_type": 2,
        "temporary": False,
        "validate": None

    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре «Fishington.io»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(91, 190, 222)))

@bot.command()
async def chess(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 832012774040141894,  # Chess
        "target_type": 2,
        "temporary": False,
        "validate": None

    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Chess In The Park»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(187, 117, 65)))

@bot.command()
async def DoodleCrew(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 878067389634314250,  # DoodleCrew
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «DoodleCrew»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(253, 194, 93)))

@bot.command()
async def doodlecrew(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 878067389634314250,  # DoodleCrew
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «DoodleCrew»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(253, 194, 93)))

@bot.command()
async def LetterTile(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 879863686565621790,  # Letter Tile
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Letter Tile»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(167, 117, 247)))

@bot.command()
async def lettertile(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 878067389634314250,  # LetterTile
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Letter Tile»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(167, 117, 247)))

@bot.command()
async def WordSnacks(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 879863686565621790,  # Word Snacks
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Word Snacks»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(254, 173, 76)))

@bot.command()
async def wordsnacks(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 879863686565621790,  # Word Snacks
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Word Snacks»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(254, 173, 76)))

@bot.command()
async def betrayal(ctx):
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 773336526917861400,  # Betrayal
        "target_type": 2,
        "temporary": False,
        "validate": None

    }
    headers = {
        "Authorization": "Bot TOKEN",
        "Content-Type": "application/json"
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send(
                embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))
    else:
        await ctx.send(
            embed = discord.Embed( title="**Пожалуйста, перейдите в голосовой канал!**", colour = 3092790))

    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)

    await ctx.send(
        embed = discord.Embed(title="Кликните, чтобы присоединиться к игре в «Betrayal.io»", url = f"https://discord.com/invite/{link['code']}", colour = discord.Colour.from_rgb(255, 222, 199)))

bot.loop.create_task(change_status())
bot.run("TOKEN")