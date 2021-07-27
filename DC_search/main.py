import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
  print('Bot is ready')

@client.command()
async def info(ctx):
  await ctx.send(' >>> **Comandos** \n/c palabra -> Buscar en el canal de **consultas sql**\n /p palabra -> Buscar en el canal de **problemas/solicitudes**\n /e palabra -> Buscar en el canal de **esquemas**')

@client.command()
async def s(ctx, *, word: str):
    channel = client.get_channel(869610627272966204)
    print(channel)
    messages = await channel.history().flatten()
    result = []
    for msg in messages:
        if word in msg.content:
            result.append(msg.content)

    if (len(result) == 0):
      await ctx.send('No hay resultados para la búsqueda')
      return

    for res in result:
      await ctx.send('>>> ' + res)

@client.command()
async def p(ctx, *, word: str):
    channel = client.get_channel(869630779569897472)
    print(channel)
    messages = await channel.history().flatten()
    result = []
    for msg in messages:
        if word in msg.content:
            result.append(msg.content)

    if (len(result) == 0):
      await ctx.send('No hay resultados para la búsqueda')
      return 

    for res in result:
      await ctx.send('>>> ' + res)

@client.command()
async def e(ctx, *, word: str):
    channel = client.get_channel(869630797257269318)
    print(channel)
    messages = await channel.history().flatten()
    result = []
    for msg in messages:
        if word in msg.content:
            result.append(msg.content)

    if (len(result) == 0):
      await ctx.send('No hay resultados para la búsqueda')
      return 

    for res in result:
      await ctx.send('>>> ' + res)

keep_alive()
client.run(os.getenv('TOKEN'))
