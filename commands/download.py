from . import command
from discord.utils import get
import discord
from discord.ext.commands import Bot
import os
import re

class Download(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Load: 'leave @role' removes role @role from user")

    async def run(self, message):
        msg = ""

        ##Categories
        msg+=("(cat,")
        categories = message.guild.categories
        for category in categories:
            msg+="{"+str(category.name)+"}"
        msg+=(")")

        ##TextChannels
        msg+=("(tc,")
        txts = message.guild.text_channels
        for txt in txts:
            msg+="{"+str(txt.category)+":"+str(txt.name)+"}"
        msg+=(")")

        ##VoiceChannels
        msg+=("(vc,")
        voices = message.guild.voice_channels
        for voice in voices:
            msg+="{"+str(voice.category)+":"+str(voice.name)+"}"
        msg+=(")")
        print(msg)
       
        