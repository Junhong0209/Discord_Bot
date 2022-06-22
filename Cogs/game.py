import discord

from discord.ext import commands
from utils.game.league_of_legend import LoLRank, LoLStats
from utils.game.overwatch import ProfileSearch, Quick, Competitive
from utils.database.index import Index
from utils.database.config import Config, ColorPalette
from utils.image.main import Image

prefix = Index.prefix


class Game(commands.Cog, name='게임'):
  f"""
  디스코드 봇(아서)의 게임 관련 명령어가 있는 카테고리입니다.
  명령어에 대한 정보를 상세히 알고 싶다면
  {prefix}도움말 [명령어]
  """
  
  def __init__(self, app):
    self.app = app

  # 현재 OP.GG 페이지의 변경으로 정상적으로 작동하지 않음. 추후 변경 예정
  @commands.command(name='롤랭크', help='소환사의 롤 랭크 점수를 보여준다.', usage=f'{prefix}롤랭크 [소환사 이름]')
  async def lol_rank(self, ctx, player_nick_name):
    embed = discord.Embed(title='Error!', color=ColorPalette.error_color)
    embed.add_field(name='Error!', value='현재 이 명령어를 사용할 수 없습니다.')
    embed.set_footer(text=Config.footer_msg, icon_url=Image.icon)

    await ctx.send(embed=embed)
    # await ctx.send(embed=LoLRank(player_nick_name).embed)
  
  # 현재 OP.GG 페이지의 변경으로 정상적으로 작동하지 않음. 추후 변경 예정
  @commands.command(name='롤전적', help='소환사의 롤 전적을 보여준다.', usage=f'{prefix}롤전적 [소환사 이름]')
  async def lol_stats(self, ctx, player_nick_name):
    embed = discord.Embed(title='Error!', color=ColorPalette.error_color)
    embed.add_field(name='Error!', value='현재 이 명령어를 사용할 수 없습니다.')
    embed.set_footer(text=Config.footer_msg, icon_url=Image.icon)

    await ctx.send(embed=embed)
    # await ctx.send(embed=LoLStats(player_nick_name).embed)
    
  @commands.command(name='OWP', help='해당 배틀태그 계정의 프로필을 보여준다.', usage=f'{prefix}OWP [배틀태그]')
  async def overwatch_profile(self, ctx, player_nick_name):
    await ctx.send(embed=ProfileSearch(player_nick_name).embed)
    
  @commands.command(name='OWS', help='해당 배틀태그 계정의 전적을 보여준다.', usage=f'{prefix}OWS [배틀태그]')
  async def overwatch_stats(self, ctx, game_mode, player_nick_name):
    if game_mode == '빠른대전':
      await ctx.send(embed=Quick(player_nick_name).embed)
    elif game_mode == '경쟁전':
      await ctx.send(embed=Competitive(player_nick_name).embed)


def setup(app):
  app.add_cog(Game(app))
