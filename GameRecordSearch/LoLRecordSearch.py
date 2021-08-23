import discord, asyncio, os, re, warnings
from discord.ext import commands
from urllib.request import URLError, HTTPError, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

import config
import Image.Image

LoLColor = config.Config.LOLColor
ErrorColor = config.Config.ErrorColor
developerImg = Image.Image.icon

tierScore = {
  'default': 0,
  'iron': 1,
  'bronze': 2,
  'silver': 3,
  'gold': 4,
  'platinum': 5,
  'diamond': 6,
  'master': 7,
  'grandmaster': 8,
  'challenger': 9
}

warnings.filterwarnings(action='ignore')

def tierCompare(solorank, flexrank):
  if tierScore[solorank] > tierScore[flexrank]:
    return 0
  elif tierScore[solorank] < tierScore[flexrank]:
    return 1
  else:
    return 2

def deleteTags(htmls):
  for a in range(len(htmls)):
    htmls[a] = re.sub('<.+?>', '', str(htmls[a]), 0).strip()
  return htmls

class LoLRecordSearch:
  def __init__(self, playerNickname):
    self.opggSummonerSearch = 'https://www.op.gg/summoner/userName='

    self.Search(playerNickname)

  def Error(self):
    self.embed = discord.Embed(title='', description='소환사의 이름이 입력되지 않았습니다.', color=ErrorColor)
    self.embed.add_field(name='Summoner name not entered', value='To use command !롤 => !롤 (Summoner Nickname', inline=False)
    self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)

  def Search(self, playerNickname):
    try:
      if not playerNickname:
        self.Error()
      else:
        # Open URL
        self.checkURLBool = urlopen(self.opggSummonerSearch + quote(playerNickname))
        self.bs = BeautifulSoup(self.checkURLBool, 'html.parser')

        # 자유랭크 언랭은 뒤에 '?image=q_auto&v=1'표현이없다

        self.Medal = self.bs.find('div', {'class': 'ChampionName'})
        self.RankMedal = self.Medal.findAll('img', {'src': re.compile('\/\/[a-z]*\-[A-Za-z]*\.[A-Za-z]*\.[A-Za-z]*\/[A-Za-z]*\/[A-Za-z]*\/[a-z0-9_]*\.png')})
        # Variable RankMedal's index 0 : Solo Rank
        # Variable RankMedal's index 1 : Flexible 5v5 rank

        # for moseUsedChampion
        self.mostUsedChampion = self.bs.find('div', {'class': 'Champion'})
        self.mostUsedChampionKDA = self.bs.find('span', {'class': 'KDA'})

        # 솔랭, 자랭 둘 다 배치가 안 되어있는 경우 => 사용된 챔피언 자체가 없다. 즉 모스트 챔피언 메뉴를 넣을 필요가 없다.

        # Scrape Summorner's Rank information
        # [Solorank, Solorank Tier]
        self.solorank_Types_and_Tier_Info = deleteTags(self.bs.findAll('div', {'class': {'RankType', 'TierRank'}}))
        # [Solorank LeaguePoint, Solorank W, Solorank L, Solorank Winratio]
        self.solorank_Point_and_winratio = deleteTags(self.bs.findAll('span', {'class': {'LeaguePoints', 'wins', 'losses', 'winratio'}}))# [Flex 5:5 Rank,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
        # [Flex 5:5 Rank,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
        self.flexrank_Types_and_Tier_Info = deleteTags(self.bs.findAll('div', {'class': {'sub-tier__rank-type', 'sub-tier__rank-tier', 'sub-tier__league-point', 'sub-tier__gray-text'}}))
        # ['Flextier W/L]
        self.flexrank_Point_and_winratio = deleteTags(self.bs.findAll('span', {'class': {'sub-tier__gray-text'}}))

        # embed.set_imag()는 하나만 들어갈수 있다.

        # 솔랭, 자랭 둘 다 배치가 안되어있는 경우 => 모스트 챔피언 출력 X
        if len(self.solorank_Point_and_winratio) == 0 and len(self.flexrank_Point_and_winratio) == 0:
          self.embed = discord.Embed(title='소환사 ' + playerNickname + '님의 전적', description='소환사 전적 검색', color=LoLColor)
          self.embed.set_thumbnail(url='httpsL'+ self.RankMedal[0]['src'])
          self.embed.add_field(name='Summoner Search From op.gg', value=self.opggSummonerSearch + playerNickname, inline=False)
          self.embed.add_field(name='Rank Solo : Unranked', value='Unranked', inline=False)
          self.embed.add_field(name='Flex 5:5 Rank : Unranked', value='Unranked', inline=False)
          self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)

        # 솔로 랭크 기록이 없는 경우
        elif len(self.solorank_Point_and_winratio) == 0:

          # 더 높은 티어를 thumnail에 안착
          self.solorankmedal = self.RankMedal[0]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')
          self.flexrankmedal = self.RankMedal[1]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')

          # Make State
          self.SoloRankTier = self.solorank_Types_and_Tier_Info[0] + ' : ' + self.solorank_Types_and_Tier_Info[1]
          self.SoloRankPointAndWinRatio = self.solorank_Point_and_winratio[0] + '/ ' + self.solorank_Point_and_winratio[1] + ' ' + self.solorank_Point_and_winratio[2] + '/ ' + self.solorank_Point_and_winratio[3]
          self.FlexRankTier = self.flexrank_Types_and_Tier_Info[0] + ' : ' + self.flexrank_Types_and_Tier_Info[1]
          self.FlexRankPointAndWinRatio = self.flexrank_Point_and_winratio[0] + '/ ' + self.flexrank_Point_and_winratio[1] + ' ' + self.flexrank_Point_and_winratio[2] + '/ ' + self.flexrank_Point_and_winratio[3]

          # most Used Champion Information : Champion Name, KDA, Win Rate
          self.mostUsedChampion = self.bs.find('div', {'class': 'ChampionName'})
          self.mostUsedChampion = self.mostUsedChampion.a.text.strip()
          self.mostUsedChampionKDA = self.bs.find('span', {'class': 'KDA'})
          self.mostUsedChampionKDA = self.mostUsedChampionKDA.text.split(':')[0]
          self.mostUsedChampionWinRate = self.bs.find('div', {'class': "Played"})
          self.mostUsedChampionWinRate = self.mostUsedChampionWinRate.div.text.strip()

          self.championTier = tierCompare(self.solorankmedal[0], self.flexrankmedal[0])
          self.embed = discord.Embed(title='소환사 ' + playerNickname + '님의 전적', description='소환사 전적 검색', color=LoLColor)
          self.embed.add_field(name='SummonerSearch From op.gg', value=self.opggSummonerSearch + playerNickname, inline=False)
          self.embed.add_field(name=self.SoloRankTier, value=self.SoloRankPointAndWinRatio, inline=False)
          self.embed.add_field(name=self.FlexRankTier, value=self.FlexRankPointAndWinRatio, inline=False)
          self.embed.add_field(name='Most Used Champion : ' + self.mostUsedChampion, value='K/D/A : ' + self.mostUsedChampionKDA + ' / ' + ' WinRate : ' + self.mostUsedChampionWinRate, inline=False)

          if self.championTier == 0:
            self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
          elif self.championTier == 1:
            self.embed.set_thumbnail(url='https:' + self.RankMedal[1]['src'])
          else:
            if self.solorankmedal[1] > self.flexrankmedal[1]:
              self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
            elif self.solorankmedal[1] < self.flexrankmedal[1]:
              self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
            else:
              self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])

          self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)

    except HTTPError as e:
      self.embed = discord.Embed(title='Wrong Summoner Nickname', description='소환사 전적 검색 실패', color=LoLColor)
      self.embed.add_field(name='???', value='올바르지 않는 소환사 이름입니다. 다시 확인해주세요!', inline=False)
      self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)

    except UnicodeError as e:
      self.embed = discord.Embed(title='Wrong Summoner Nickname', description='소환사 전적 검색 실패', color=LoLColor)
      self.embed.add_field(name='해당 닉네임의 소환사가 존재하지 않습니다.', value='소환사 이름을 확인해주세요.', inline=False)
      self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)

    except AttributeError as e:
      self.embed = discord.Embed(title='Error : Non existing Summoner', description='존재하지 않는 소환사', color=LoLColor)
      self.embed.add_field(name='해당 닉네임의 소환사가 존재하지 않습니다.', value='소환사 이름을 확인해주세요.', inline=False)
      self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)