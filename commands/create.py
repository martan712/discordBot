from . import command
from discord.utils import get
import discord
from discord.ext.commands import Bot
import os

class Create(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Create: 'leave @role' removes role @role from user")

    async def run(self, message):
        messagesplit = message.content.split()
        if(len(messagesplit)==3):

            if(messagesplit[1] == "vc" or messagesplit[1] == "tc"):
                for x in range(3):
                    if(messagesplit[1] == "vc"):
                        channel = await message.guild.create_voice_channel(messagesplit[2])
                        
                    elif(messagesplit[1] == "tc"):
                        channel = await message.guild.create_text_channel(messagesplit[2])

                    name = "test"
                    category = discord.utils.get(message.guild.categories, name=name)
                    await channel.edit(category=category) 
        else:
            await message.channel.send("Please use the correct syntax: 'create [channteltype] [channelname]'")