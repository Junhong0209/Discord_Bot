import discord
import os.path

from discord.ext import commands
from utils.database.index import Index
from utils.database.config import ColorPalette, Config
from utils.image.main import Image

prefix = Index.prefix
color = ColorPalette.main_color
msg = Config.footer_msg
icon = Image.icon
error_emoji = ':exclamation:'
check_emoji = ':white_check_mark:'
file = 'Utils/Database/channel.txt'


class Admin(commands.Cog, name='관리자'):

  def __init__(self, app):
    self.app = app

  @commands.command(name='권한', help='해당 서버에서 관리자 권한이 있는지 확인한다', usage=f'{prefix}권한')
  async def admin_check(self, ctx):
    if ctx.guild:
      if ctx.message.author.guild_permissions.administrator:
        await ctx.send(f'{check_emoji} {ctx.author.mention}님, 이 서버에서 관리자 권한을 가지고 있습니다.')
      else:
        await ctx.send(f'{error_emoji} {ctx.author.mention}님, 이 서버에서 관리자 권한을 가지고 있지 않습니다.')
    else:
      await ctx.send(f'{error_emoji} {ctx.author.mention}님, DM으로 관리자 권한 체크를 할 수 없습니다.')

  @commands.command(name='채널설정', help='공지 작성을 위한 채널 설정을 한다', usage=f'{prefix}채널설정 [#채널 명]')
  async def channel_setting(self, ctx, channel: discord.TextChannel):
    if ctx.guild:
      if ctx.message.author.guild_permissions.administrator:
        if os.path.isfile(file):
          f = open(file, 'w', encoding='utf-8')
          f.write(str(channel.id))
          f.close()
          await ctx.send(f'{check_emoji} ``{channel}``로 공지 채널이 재설정되었습니다.')
        else:
          f = open(file, 'w', encoding='utf-8')
          f.write(str(channel.id))
          f.close()
          await ctx.send(f'{check_emoji} ``{channel}``로 공지 채널이 설정되었습니다.')
      else:
        await ctx.send(f'{error_emoji} {ctx.author.mention}님, 관리자 권한이 없습니다.')
    else:
      await ctx.send(f"{error_emoji} {ctx.author.mention}님, DM으론 불가능 합니다.")

  @commands.command(name='공지작성', help='설정한 채널에 공지를 작성합니다.', usage=f'{prefix}공지작성 [할 말]')
  async def announcement(self, ctx, *, notice):
    if ctx.guild:
      if ctx.message.author.guild_permissions.administrator:
        try:
          f = open(file, 'r', encoding='utf-8')
          channel = ctx.guild.get_channel(int(f.read()))
          embed = discord.Embed(title=f'**{ctx.guild.name} 공지사항**', color=color)
          embed.add_field(name='공지 사항은 항상 잘 숙지 해주시기 바랍니다.', value=f'‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n{notice}\n\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
          embed.set_footer(text=f'{msg} | 공지 작성자: {ctx.author}', icon_url=icon)
          await channel.send(embed=embed)
          await ctx.send(f'```** [ BOT 자동 알림 ] **\n정상적으로 공지가 채널에 작성이 되었습니다. :)\n\n[ 공지 작성자 ]: {ctx.author}\n\n[ 공지 내용 ]: {notice}```')
        except FileNotFoundError:
          await ctx.send(f'{error_emoji} 공지를 작성할 채널을 먼저 설정해주세요!')
      else:
        await ctx.send(f'{error_emoji} {ctx.author.mention}님, 관리자 권한이 없습니다.')
    else:
      await ctx.send(f'{error_emoji} {ctx.author.mention}님, DM으론 불가능 합니다.')


def setup(app):
  app.add_cog(Admin(app))
