from . import command
from discord.utils import get
import discord
from discord.ext.commands import Bot
import os
import re

async def getPairs(message):
    result = []
    res = re.findall(r'\(.*?\)', message)
    for x in res:
        result.append(x[1:len(x)-1])
    return result

async def getValues(message):
    result = []
    res = re.findall(r'\{.*?\}', message)
    for x in res:
        result.append(x[1:len(x)-1])
    return result

class Load(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Load: 'leave @role' removes role @role from user")

    async def run(self, message):
        msg = input()
        msg = msg.replace(" ", "") 
        params = await getPairs(msg)
        for x in params:
            kind, values = x.split(",")
            values = await getValues(values)
            if (kind == "cat"):
                for value in values:
                    await message.guild.create_category(value)
            if (kind == "vc"):
                for value in values:
                    categoryName, name = value.split(":")
                    category = discord.utils.get(message.guild.categories, name=categoryName)
                    channel = await message.guild.create_voice_channel(name, category=category)
            if (kind == "tc"):
                for value in values:
                    categoryName, name = value.split(":")
                    category = discord.utils.get(message.guild.categories, name=categoryName)
                    channel = await message.guild.create_text_channel(name, category=category)
