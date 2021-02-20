from . import command
from discord.utils import get

class Join(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Join: 'join @role' adds role @role to user")

    async def run(self, message):
        messagesplit = message.content.split()
        role_id_full = messagesplit[1]
        role_id = int(role_id_full[3:len(role_id_full)-1])
        role = get(message.guild.roles, id=role_id)
        await message.author.add_roles(role)