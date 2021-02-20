import discord
from discord.ext.commands import Bot
import os
from commands import *

bot = Bot("!")

helpmessage = []

## COMMANDS ##
ping = Ping(helpmessage)
join = Join(helpmessage)
leave = Leave(helpmessage)
create = Create(helpmessage)
load = Load(helpmessage)
download = Download(helpmessage)
clear = Clear(helpmessage)

async def sendHelp(message):
    for line in helpmessage:
         await message.channel.send(line)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    

    if message.author == bot.user:
        return

    if message.content.startswith('!help'):
        await sendHelp(message)

    if message.content.startswith('!ping'):
        await ping.run(message)

    if message.content.startswith('!join'):
        await join.run(message)

    if message.content.startswith('!leave'):
        await leave.run(message)

    if message.content.startswith('!create'):
        await create.run(message)

    if message.content.startswith('!load'):
        await load.run(message)

    if message.content.startswith('!download'):
        await download.run(message)

    if message.content.startswith('!clear'):
        await clear.run(message)

    if message.content.startswith('!hello'):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.set_image(url='https://cdn1.thr.com/sites/default/files/2012/12/img_logo_blue.jpg')
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)
        
bot.run("ODEyMzA3NTk5Mzc0Mjg2OTA4.YC-2Zw.jrNkDR-LS_iEm2ati4O9PPNyr6g")

@bot.command(pass_context=True)
async def SendMessage(ctx):
    await ctx.send('Hello')