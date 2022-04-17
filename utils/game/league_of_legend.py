import discord
import requests

from bs4 import BeautifulSoup
from utils.config.main import BS4, ColorPalette

protocol = BS4.Protocol
headers = BS4.Headers
cookies = BS4.Cookies

LoLColor = ColorPalette.league_of_legend_color


class LoLRank:
  def __init__(self, player_nick_name):
    self.soloRank = None
    self.soloRankType = None
    self.soloRankTier = None
    self.soloRankTierPoint = None
    self.soloRankWin = None
    self.soloRankLose = None
    self.soloRankWinRate = None
    self.flexRank = None
    self.flexRankType = None
    self.flexRankTier = None
    self.flexRankTierPoint = None
    self.flexRankWinRate = None
    self.playerNickName = player_nick_name.replace(' ', '%20')
    self.url = f'{protocol}www.op.gg/summoner/userName={self.playerNickName}'
    
    self.req = requests.get(self.url)
    self.html = self.req.text
    self.soup = BeautifulSoup(self.html, 'html.parser')
    
    self.playerIcon = self.soup.find('img', {'class': 'ProfileImage'})['src'].replace('//', '')
    self.playerLevel = self.soup.find('span', {'class': 'Level'}).text
    
    self.embed = discord.Embed(title=self.playerNickName.replace('%20', ' ') + '님의 랭크', description=f'Level: {self.playerLevel}\n{self.url}\n↑ 직접 확인하기\n', color=LoLColor)
    self.embed.set_thumbnail(url=f'{protocol}{self.playerIcon}')
    
    self.rank()

  def rank(self):
    try:
      self.soloRank = self.soup.find('div', {'class': 'TierRankInfo'})
      self.soloRankType = self.soup.find('div', {'class': 'RankType'}).text.replace('솔로', '솔로 ')
      self.soloRankTier = self.soloRank.find('div', {'class': 'TierRank'}).text.replace('\n', '')
      self.soloRankTierPoint = self.soloRank.find('span', {'class': 'LeaguePoints'}).text.replace('\n', '').replace('\t', '').replace(' L ', 'L')
      self.soloRankWin = self.soloRank.find('span', {'class': 'wins'}).text.replace('\n', '')
      self.soloRankLose = self.soloRank.find('span', {'class': 'losses'}).text.replace('\n', '')
      self.soloRankWinRate = self.soloRank.find('span', {'class': 'win ratio'}).text
      self.embed.add_field(name=self.soloRankType, value=f'티어: {self.soloRankTier} / {self.soloRankTierPoint}\n승패: {self.soloRankWin} {self.soloRankLose} ({self.soloRankWinRate})')
    except AttributeError:
      self.embed.add_field(name=self.soloRankType, value=f'티어: {self.soloRankTier}')

    try:
      self.flexRank = self.soup.find('div', {'class': 'sub-tier__info'})
      self.flexRankType = self.flexRank.find('div', {'class': 'sub-tier__rank-type'}).text
      self.flexRankTier = self.flexRank.find('div', {'class': 'sub-tier__rank-tier'}).text.replace('\n', '').replace('  ', '')
      self.flexRankTierPoint = self.flexRank.find('div', {'class': 'sub-tier__league-point'}).text.replace('P/', 'P /').split(' / ')
      self.flexRankWinRate = self.flexRank.find('div', {'class': 'sub-tier__gray-text'}).text.replace('\n', '').replace('  ', '')
      self.embed.add_field(name=self.flexRankType, value=f'티어: {self.flexRankTier} / {self.flexRankTierPoint[0]}\n승패: {self.flexRankTierPoint[1]} ({self.flexRankWinRate})')
    except AttributeError:
      self.embed.add_field(name=self.flexRankType, value=f'티어: {self.flexRankTier}')


class LoLStats:
  def __init__(self, player_nick_name):
    self.playerNickName = player_nick_name.replace(' ', '%20')
    self.url = f'{protocol}www.op.gg/summoner/userName={self.playerNickName}'
    
    self.req = requests.get(self.url, headers=headers, cookies=cookies)
    self.html = self.req.text
    self.soup = BeautifulSoup(self.html, 'html.parser')
    
    self.playerIcon = self.soup.find('img', {'class': 'ProfileImage'})['src'].replace('//', '')
    self.playerLevel = self.soup.find('span', {'class': 'Level'}).text
    
    self.winRatio = self.soup.find('div', {'class': 'WinRatioTitle'}).text.replace('\n', '').replace('\t', '').replace('전', '전 ').replace('승', '승 ')
    self.winRate = self.soup.find('div', {'class': 'Text'}).text
    
    self.soloRank = self.soup.find('div', {'class': 'TierRankInfo'})
    self.soloRankTier = self.soloRank.find('div', {'class': 'TierRank'}).text.replace('\n', '').replace('\t', '').replace('  ', '')
    
    self.flexRank = self.soup.find('div', {'class': 'sub-tier__info'})
    self.flexRankTier = self.flexRank.find('div', {'class': 'sub-tier__rank-tier'}).text.replace('\n', '').replace('\t', '').replace('  ', '')
    
    self.gameStats = self.soup.find_all('div', {'class': 'GameStats'})
    self.gameSettingInfo = self.soup.find_all('div', {'class': 'GameSettingInfo'})
    self.KDA = self.soup.find_all('div', {'class': 'KDA'})
    self.stats = self.soup.find_all('div', {'class': 'Stats'})
    
    self.embed = discord.Embed(title=self.playerNickName.replace('%20', ' ') + '님의 전적', description=f'Level: {self.playerLevel}\n{self.url}\n↑ 직접 확인하기\n', color=LoLColor)
    self.embed.set_thumbnail(url=f'{protocol}{self.playerIcon}')
    
    self.gameType = []
    self.gameResult = []
    self.gameLength = []
    self.timeStamp = []
    self.championName = []
    self.level = []
    self.CS = []
    self.CKRate = []
    self.killDeathAssist = []
    self.KDARatio = []
    
    self.player_stats()

  def player_stats(self):
    for i in range(30):
      try:
        if i < 5:
          self.gameType.append(self.gameStats[i].find('div', {'class': 'GameType'}).text.replace('\n', '').replace('\t', ''))  # 게임 종류 (일반, 솔로 랭크, 자유 5:5 랭크)
          self.gameResult.append(self.gameStats[i].find('div', {'class': 'GameResult'}).text.replace('\n', '').replace('\t', ''))  # 게임 승/패
          self.gameLength.append(self.gameStats[i].find('div', {'class': 'GameLength'}).text)  # 인게임 플레이 시간
          self.timeStamp.append(self.gameStats[i].find('div', {'class': 'TimeStamp'}).text)  # 플레이한 시간 (현실 시간)
          self.championName.append(self.gameSettingInfo[i].find('div', {'class': 'ChampionName'}).text.replace('\n', ''))  # 챔피언 이름
          self.level.append(self.stats[i].find('div', {'class': 'Level'}).text.replace('\n', '').replace('\t', ''))  # level
          self.CS.append(self.stats[i].find('div', {'class': 'CS'}).text.replace('\n', '').replace('\t', ''))  # CS
          self.CKRate.append(self.stats[i].find('div', {'class': 'CKRate'}).text.replace('\n', '').replace('\t', ''))  # 킬관여
        if self.soloRankTier == 'Unranked' and self.flexRankTier == 'Unranked':
          try:
            if len(self.killDeathAssist) < 5:
              self.killDeathAssist.append(self.KDA[i].find('div', {'class': 'KDA'}).text.replace('\n', '').replace('\t', '').replace(' ', ''))  # 킬/뎃/어시
              self.KDARatio.append(self.KDA[i].find('span', {'class': 'KDARatio'}).text.replace(':1', ':1 평점'))  # 평점
          except AttributeError:
            pass
        else:
          try:
            if len(self.killDeathAssist) < 5:
              self.killDeathAssist.append(self.KDA[i].find('div', {'class': 'KDA'}).text.replace('\n', '').replace('\t', '').replace(' ', ''))
              self.KDARatio.append(self.KDA[i].find('span', {'class': 'KDARatio'}).text.replace(':1', ':1 평점'))
          except AttributeError:
            pass
      except IndexError:
        break

    for i in range(len(self.gameType)):
      self.embed.add_field(name=f'{self.gameType[i]} ({self.championName[i]} {self.level[i]})', value=f'({self.timeStamp[i]}에 플레이한 게임)\n승패: {self.gameResult[i]} / 플레이 시간: {self.gameLength[i]}\nKDA: {self.killDeathAssist[i]} / 킬관여: {self.CKRate[i]} / CS: {self.CS[i]}', inline=False)
