from server import keep_alive
from discord.ext import tasks
import os
import discord
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def reply(message):
  reply = f'{message.author.mention}お呼びでしょうか？'  # 返信メッセージの作成
  await message.channel.send(reply)  # 返信メッセージを送信


async def greet():
  channel = client.get_channel(1062192778240589847)
  await channel.send('おはようございます')


@tasks.loop(seconds=1)
async def loop():
  print('loopできてる')
  # await client.wait_until_ready()
  # channel = client.get_channel(1062192778240589847)
  # await channel.send('時間だよ')


async def fn():
  await loop.start()


@client.event
async def on_ready():
  print('Botがログインしました')

  await greet()


@client.event
async def on_message(message):
  if message.author.bot:
    return

  if message.content == 'おはよう':
    await message.channel.send(f'おはようございます {message.author.name}様')

  if client.user in message.mentions:
    await message.channel.send(f'お呼びでしょうか {message.author.name}様')
    await reply(message)


@client.event
async def on_voice_status_update(member, before, after):
  return


keep_alive()
loop_ = asyncio.get_event_loop()
loop_.run_until_complete(fn())
my_secret = os.environ['TOKEN']
client.run(my_secret)
