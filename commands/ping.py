from . import command

class Ping(command.Command):
    def __init__(self, helpmessage):
        helpmessage.append("Ping: Server should reply with 'pong'")

    async def run(self, message):
        await message.channel.send("Pong!")