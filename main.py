import asyncio
import discord
import os

from discord.ext import commands
from utils.config.main import Time
from utils.database.main import Main

app = commands.Bot(command_prefix=Main.prefix)

token = os.environ.get('discord_token')

for filename in os.listdir('Cogs'):
  if filename.endswith('.py'):
    app.load_extension(f'Cogs.{filename[:-3]}')

@app.event
async def on_ready():
  try:
    try:
      f = open('Utils/Database/bot_log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
      f = open('Utils/Database/bot_log.txt', 'w', encoding='utf-8')

    print(f'Loggend-in Bot: {app.user.name}\nBot id: {app.user.id}\nconnection was successful\n{Time.get_time()}\n' + '=' * 30 + '\n')
    f.write((f'Loggend-in Bot: {app.user.name}\nBot id: {app.user.id}\nconnection was successful\n{Time.get_time()}\n' + '=' * 30 + '\n'))
    f.close()

    game = discord.Game('정신 차리기')
    await app.change_presence(status=discord.Status.idle, activity=game)
    await asyncio.sleep(5)
    while True:
      game = discord.Game('빡추 스탯 쌓기')
      await app.change_presence(status=discord.Status.online, activity=game)
      await asyncio.sleep(3)
      game = discord.Game('여전히 테스트 중 이에요~')
      await app.change_presence(status=discord.Status.online, activity=game)
      await asyncio.sleep(3)
      game = discord.Game('테스트가 끝나긴 할까요~')
      await app.change_presence(status=discord.Status.online, activity=game)
      await asyncio.sleep(3)
      game = discord.Game(f'{Main.prefix}도움말')
      await app.change_presence(status=discord.Status.online, activity=game)
      await asyncio.sleep(3)
  except ConnectionResetError:
    try:
      f = open('Utils/Database/bot_log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
      f = open('Utils/Database/bot_log.txt', 'w', encoding='utf-8')

    print(f'Log out Bot\nConnection Reset Error.\nRestart Please.\n{Time.get_time()}\n' + '=' * 30 + '\n')
    f.write(f'Log out Bot\nConnection Reset Error.\nRestart Please.\n{Time.get_time()}\n' + '=' * 30 + '\n')
    f.close()


@app.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('존재하지 않는 명령어입니다.')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('값을 입력해주세요.')
  elif isinstance(error, commands.BadArgument):
    await ctx.send('값이 다릅니다.')
  else:
    embed = discord.Embed(title='Error!!', description='An Error has occurred.', color=0xFF0000)
    embed.add_field(name='Detailed Error', value=f'```{error}```')
    await ctx.send(embed=embed)


@app.command(name='리로드')
async def reload_commands(ctx, extension=None):
  if extension is None:
    for file_name in os.listdir("Cogs"):
      if file_name.endswith(".py"):
        app.unload_extension(f"Cogs.{file_name[:-3]}")
        app.load_extension(f"Cogs.{file_name[:-3]}")
    await ctx.send(":white_check_mark: 모든 명령어를 다시 불러왔습니다!")
  else:
    app.unload_extension(f'Cogs.{extension}')
    app.load_extension(f'Cogs.{extension}')
    await ctx.send(f':white_check_mark: {extension}을(를) Reload 했습니다!')

app.run(token)