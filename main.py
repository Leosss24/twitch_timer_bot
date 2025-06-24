import asyncio
from twitchio.ext import commands
import os

BOT_NICK = os.getenv('BOT_NICK')
CHANNEL = os.getenv('CHANNEL')
TOKEN = os.getenv('TWITCH_TOKEN')

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=TOKEN,
            nick=BOT_NICK,
            prefix='!',
            initial_channels=[CHANNEL]
        )

    async def event_ready(self):
        print(f'Bot conectado como | {self.nick}')

    async def event_message(self, message):
        if message.author.name.lower() == BOT_NICK.lower():
            return
        await self.handle_commands(message)

    @commands.command(name='pizza')
    async def pizza_command(self, ctx):
        try:
            minutos = int(ctx.message.content.split(' ')[1])
            await ctx.send(f'Se ha iniciado un temporizador de {minutos} minutos')
            await asyncio.sleep(minutos * 60)
            await ctx.send(f'Temporizador de {minutos} minutos finalizado')
        except (IndexError, ValueError):
            await ctx.send('Error: usa !pizza seguido de un número. Ej: !pizza 15')

if __name__ == '__main__':
    bot = Bot()
    bot.run()
