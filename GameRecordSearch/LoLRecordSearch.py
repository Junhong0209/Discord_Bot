import discord, asyncio, os, re, warnings
from discord.ext import commands
from urllib.request import URLError, HTTPError, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

from config import Config as config
from Image import Image as image

LoLColor = config.LoLColor
ErrorColor = config.ErrorColor
developerImg = image.icon
footerMsg = config.FooterMsg

warnings.filterwarnings(action='ignore')

class LoLRecordSearch:
  def __init__(self, playerNickname):
    self.tierScore = {
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
    self.opggSummonerSearchUrl = 'https://www.op.gg/summoner/userName='
    self.playerNickname = playerNickname

    try:
      if not playerNickname:
        self.Error()
      else:
        # Open URL
        self.checkURLBool = urlopen(self.opggSummonerSearchUrl + quote(playerNickname))
        self.bs = BeautifulSoup(self.checkURLBool, 'html.parser')

        # 자유랭크 언랭은 뒤에 '?imgae=q_auto&v=1' 표현이 없다.
        self.Medal = self.bs.find('div', {'class': 'SideContent'})
        print(self.Medal)
        self.RankMedal = self.Medal.find_all('img', {
          'src': re.compile('\/\/[a-z]*\-[A-Za-z]*\.[A-Za-z]*\.[A-Za-z]*\/[A-Za-z]*\/[A-Za-z]*\/[a-z0-9_]*\.png')})
        print(self.RankMedal)
        # Variable RankMedal's index 0 : Solo Rank
        # Variable RankMedal's index 1 : Flexible 5v5 Rank

        # for mostUsedChampiton
        self.mostUsedChampion = self.bs.find('div', {'class': 'ChampionName'})
        self.mostUsedChampionKDA = self.bs.find('span', {'class': 'KDA'})

        # 솔랭, 자랭 둘 다 배치가 안되어 있는 경우 => 사용된 챔피언 자체가 없다. 즉 모스트 챔피언 메뉴를 넣을 필요가 없다.

        # Scrape Summoner's Rank information
        # [SoloRank, SoloRank Tier]
        self.solorank_Types_and_Tier_info = self.deleteTags(self.bs.find('div', {'class': {'RankType', 'TierRank'}}))
        print(self.solorank_Types_and_Tier_info)
        # [Solorank LeaguePoint, Solorank W, Solorank L, Solorank Winratio]
        self.solorank_Point_and_winratio = self.deleteTags(self.bs.find('span', {'class': {'LeaguePoints', 'wins', 'losses', 'winratio'}}))
        # [Flex 5:5 Rank,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
        self.flexrank_Types_and_Tier_info = self.deleteTags(self.bs.find('div', {'class': {'sub-tier__rank-type', 'sub-tier__league-point', 'sub-tier__gray-text'}}))
        # ['Flextier W/L]
        self.flexrank_Point_and_winratio = self.deleteTags(self.bs.find('span', {'class': {'sub-tier__gray-text'}}))

        # embed.set_image()는 하나만 들어갈 수 있다.

        if len(self.solorank_Point_and_winratio) == 0 and len(self.flexrank_Point_and_winratio) == 0:
          self.NoSolorankNoFlexrank()

        elif len(self.solorank_Point_and_winratio) == 0:
          # 더 높은 티어를 thumnail에 안착
          self.soloRankMedal = self.RankMedal[0]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')
          self.flexRankMedal = self.RankMedal[1]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')

          # Make State
          self.soloRankTier = self.solorank_Types_and_Tier_info[0] + ' : ' + self.solorank_Types_and_Tier_info[1]
          self.soloRankPointAndWinratio = self.solorank_Point_and_winratio[0] + ' / ' + self.solorank_Point_and_winratio[1] + ' ' + self.solorank_Point_and_winratio[2] + '/ ' + self.solorank_Point_and_winratio[3]
          self.flexRankTier = self.flexrank_Types_and_Tier_info[0] + ' : ' + self.flexrank_Types_and_Tier_info[1]
          self.flexRankPointAndWinratio = self.flexrank_Point_and_winratio[0] + ' / ' + self.flexrank_Point_and_winratio[1] + ' ' + self.flexrank_Point_and_winratio[2] + '/ ' + self.flexrank_Point_and_winratio[3]

          # most Used Champion Informaion : Champion Name, KDA, Win Rate
          self.mostUsedChampion = self.bs.find('div', {'class': 'ChampionName'})
          self.mostUsedChampion = self.mostUsedChampion.a.text.strip()
          self.mostUsedChampionKDA = self.bs.find('span', {'class': 'KDA'})
          self.mostUsedChampionKDA = self.mostUsedChampionKDA.text.split(':')[0]
          self.mostUsedChampionWinRate = self.bs.find('div', {'class': 'Played'})
          self.mostUsedChampionWinRate = self.mostUsedChampionWinRate.div.text.strip()

          self.championTier = self.tierScore(self.soloRankMedal[0], self.flexRankMedal[0])
          self.NoSolorank()

    except HTTPError as e:
      self.HttpError()
      print(e)

    except UnicodeError as e:
      self.UnicodeError()
      print(e)

    except AttributeError as e:
      self.AttributeError()
      print(e)

  def tierCompare(self, soloRank, flexRank):
    if self.tierScore[soloRank] > self.tierScore[flexRank]:
      return 0
    elif self.tierScore[soloRank] < self.tierScore[flexRank]:
      return 1
    else:
      return 2

  def deleteTags(self, htmls):
    for a in range(len(htmls)):
      htmls[a] = re.sub('<.+?>','',str(htmls[a]),0).strip()
    return htmls

  def Error(self):
    self.embed = discord.Embed(title='입력 오류!', description='소환사의 이름이 입력되지 않았습니다.', color=ErrorColor)
    self.embed.add_field(name='Summoner name not enterd', value='To use command !롤 => !롤 [Summoner Nickname]', inline=False)
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)

  def NoSolorankNoFlexrank(self):
    self.embed = discord.Embed(title='소환사 ' + self.playerNickname + '님의 전적', description='소환사 전적 검색', color=LoLColor)
    self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
    self.embed.add_field(name='Summoner Search From op.gg', value=self.opggSummonerSearchUrl + self.playerNickname)
    self.embed.add_field(name='Rank Solo: Unranked', value='Unranked', inline=False)
    self.embed.add_field(name='Flex 5:5Rank: Unranked', value='Unranked', inline=False)
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)

  def NoSolorank(self):
    self.embed = discord.Embed(title='소환사 ' + self.playerNickname + '님의 전적', description='소환사 전적 검색', color=LoLColor)
    self.embed.add_field(name='SummonerSearch From op.gg', value=self.opggSummonerSearchUrl + self.playerNickname)
    self.embed.add_field(name=self.soloRankTier, value=self.soloRankPointAndWinratio + self.playerNickname, inline=False)
    self.embed.add_field(name=self.flexRankTier, value=self.flexRankPointAndWinratio + self.playerNickname, inline=False)
    self.embed.add_field(name='Most Used Champion: ' + self.mostUsedChampion, value='K/D/A : ' + self.mostUsedChampionKDA + ' / ' + 'WinRate : ' + self.mostUsedChampionWinRate, inline=False)

    # 임베드 thumnail 설정
    if self.championTier == 0:
      self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
    elif self.championTier == 1:
      self.embed.set_thumbnail(url='https:' + self.RankMedal[1]['src'])
    else:
      if self.soloRankMedal[1] > self.flexRankMedal[1]:
        self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
      elif self.soloRankMedal[1] < self.flexRankMedal[1]:
        self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])
      else:
        self.embed.set_thumbnail(url='https:' + self.RankMedal[0]['src'])

    # 임베드 제일 하단 부분 설정
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)

  def HttpError(self):
    self.embed = discord.Embed(title='Worng Summoner Nickname', description='소환사 전적 검색 실패', color=ErrorColor)
    self.embed.add_field(name='???', value='올바르지 않는 소환사 이름 입니다. 다시 한번 확인해주세요!', inline=False)
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)

  def UnicodeError(self):
    self.embed = discord.Embed(title='Wrong Summoner Nickname', description='소환사 전적 검색 실패', color=LoLColor)
    self.embed.add_field(name='해당 닉네임의 소환사가 존재하지 않습니다.', value='소환사 이름을 확인해주세요.', inline=False)
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)

  def AttributeError(self):
    self.embed = discord.Embed(title='Error : Non existing Summoner', description='존재하지 않는 소환사', color=LoLColor)
    self.embed.add_field(name='해당 닉네임의 소환사가 존재하지 않습니다.', value='소환사 이름을 확인해주세요.', inline=False)
    self.embed.set_footer(text=footerMsg, icon_url=developerImg)