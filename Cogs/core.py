import os
import discord

from discord.ext import commands
from utils.config.main import ColorPalette, Config
from utils.image.main import Image
from utils.database.main import Main

color = ColorPalette.main_color
ErrorColor = ColorPalette.error_color
msg = Config.footer_msg
icon = Image.icon
prefix = Main.prefix


class Core(commands.Cog, name='기본'):
  f"""
  디스코드 봇(아서)의 기본 명령어가 있는 카테고리입니다.
  명령어에 대한 정보를 상세히 알고 싶다면
  {prefix}도움말 [명령어]
  """
  
  def __init__(self, app):
    self.app = app

  @commands.command(name='순서', help='순서를 설정합니다. 띄어쓰기로 구분합니다.', usage=f'{prefix}순서 or {prefix}순서 [이름] [이름].... or {prefix}순서 초기화')
  async def set_number(self, ctx, *, text=None):
    if text == None:
      try:
        f = open('Utils/Database/setNumber.txt', 'r', encoding='utf-8')
        embed = discord.Embed(title='순서', color=color)
        for value in enumerate(f.read().split(' ')):
          embed.add_field(name=value[0] + 1, value=value[1], inline=False)
        f.close()
        await ctx.send(embed=embed)
      except FileNotFoundError:
        embed = discord.Embed(title='Error!', color=ErrorColor)
        embed.add_field(name='Error!', value='저장되어있는 순서가 존재하지 않습니다.')
        embed.set_footer(text=msg, icon_url=icon)
        await ctx.send(embed=embed)
    elif text=='초기화':
      try:
        os.remove('Utils/Database/setNumber.txt')
        embed = discord.Embed(title='Success!', color=color)
        embed.add_field(name='성공적으로 삭제 되었습니다!', value='값이 성공적으로 초기화 되었습니다.')
        embed.set_footer(text=msg, icon_url=icon)
        await ctx.send(embed=embed)
      except:
        embed = discord.Embed(title='Error!', color=ErrorColor)
        embed.add_field(name='Error!', value='이미 파일이 존재하지 않습니다.')
        embed.set_footer(text=msg, icon_url=icon)
        await ctx.send(embed=embed)
    else:
      try:
        f = open('Utils/Database/setNumber.txt', 'w', encoding='utf-8')
      except FileNotFoundError:
        f = open('Utils/Database/setNumber.txt', 'w', encoding='utf-8')
      f.write(text)
      f.close()
      embed = discord.Embed(title='Success!', color=color)
      embed.add_field(name='저장되었습니다!', value=f'순서가 저장되었습니다.\n순서를 확인하고 싶으시면 {prefix}순서를 입력해주세요.')
      embed.set_footer(text=msg, icon_url=icon)
      await ctx.send(embed=embed)


  @commands.command(name='출력', help='출력을 합니다', usage=f'{prefix}출력')
  async def print_it(self, ctx):
    await ctx.send(":) Python Bot에 의해 출력")
    
  @commands.command(name='따라하기')
  async def echo(self, ctx, *, content):
    await ctx.send(content)
    
  @commands.command(name='제작자', help='제작자의 정보를 알려줍니다', usage=f'{prefix}제작자')
  async def developer(self, ctx):
    embed = discord.Embed(title='제작자 정보', color=color)
    embed.add_field(name='Discord', value='빨강고양이#5278', inline=False)
    embed.add_field(name='GitHub', value='[제작자의 GitHub](https://github.com/Junhong0209)', inline=False)
    embed.add_field(name='Facebook', value='[제작자의 Facebook](https://www.facebook.com/Junhong04/)', inline=False)
    embed.add_field(name='Instagram', value='[제작자의 Instagram](https://www.instagram.com/Junhong936/)', inline=False)
    embed.add_field(name='Blog', value='[제작자의 Blog](https://dev-radcat.tistory.com/)', inline=False)
    embed.set_footer(text=msg, icon_url=icon)
    await ctx.send(embed=embed)
    
  @commands.command(name='빡추', help='들어간 이름이 빡추 스탯을 쌓는다.', usage=f'{prefix}빡추 [이름]')
  async def idiot(self, ctx, *, name=None):
    if name is None:
      await ctx.send('누구를 입력하신거죠? 입력 받은게 없습니다만?')
    elif name.find('아서') or name.find('봇') or name.find('me') or name.find('저') or name.find('이 몸'):
      await ctx.send('ㅋ')
    else:
      await ctx.send(f'보셨나요?? 보셨나요?? 보셨냐구요!!! {name}의 빡추 스탯 쌓기!!')

  @commands.command(name='도움말', help='모든 명령어와 명령어에 대한 설명을 보여줍니다', uasge=f'{prefix}도움말 or {prefix}도움말 [카테고리 명 or 명령어]')
  async def help_command(self, ctx, func=None):
    cog_list = ["기본", "게임", "급식", "관리자"]
    if func is None:
      embed = discord.Embed(title='아서봇 도움말', description=f'접두사는 {prefix}입니다\n상세 명령어를 알고 싶다면\n{prefix}도움말 [명령어 명, 카테고리 명]', color=color)
      embed.set_footer(text=msg, icon_url=icon)
      for x in cog_list:
        cog_data = self.app.get_cog(x)
        command_list = cog_data.get_commands()
        embed.add_field(name=f'카테고리: {x}\n' + '‾' * 20, value=', '.join([c.name for c in command_list]), inline=False)
      await ctx.send(embed=embed)
    else:
      message_send = False  # 메세지를 보냈는 지 확인하는 변수
      for _title, cog in self.app.cogs.items():
        if func in cog_list:
          cog_data = self.app.get_cog(func)
          command_list = cog_data.get_commands()
          embed = discord.Embed(title=f"카테고리 : {cog_data.qualified_name}", description=cog_data.description, color=color)
          embed.add_field(name="명령어들", value=", ".join([c.name for c in command_list]))
          embed.set_footer(text=msg, icon_url=icon)
          await ctx.send(embed=embed)
          message_send = True  # 메세지를 보냈다면 True
          break
        else:
          for title in cog.get_commands():
            if title.name == func:
              cmd = self.app.get_command(title.name)
              embed = discord.Embed(title=f"명령어 : {cmd}", description=cmd.help, color=color)
              embed.add_field(name="사용법", value=cmd.usage)
              embed.set_footer(text=msg, icon_url=icon)
              await ctx.send(embed=embed)
              message_send = True  # 메세지를 보냈다면 True
              break
      if not message_send:
        await ctx.send('그런 이름의 명령어나 카테고리는 존재하지 않습니다.')


def setup(app):
  app.add_cog(Core(app))
