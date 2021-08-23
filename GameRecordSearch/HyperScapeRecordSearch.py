import discord
from bs4 import BeautifulSoup
import requests

from config import Config as config
from Image import Image as image

HyperScapeColor = config.HyperScapeColor
ErrorColor = config.ErrorColor

delvoperIcon = image.icon

class HyperScapeRecordSearch:
  platformLink = "uplay/ or psn/ or xbl/"
  platform = "PC or PS4 or XBOX"

  def __init__(self, playerNickname):
    self.webpage = requests.get('https://tracker.gg/hyper-scape/profile/' + self.platformLink + playerNickname +'/overview')
    self.html = self.webpage.text
    self.soup = BeautifulSoup(self.html, 'html.parser')

    self.kda = None
    self.wins = None
    self.winrate = None
    self.avgservivaltime = None
    self.crownrate = None
    self.crownwins = None
    self.kills = None
    self.assists = None
    self.chests = None
    self.fusions = None
    self.revives = None
    self.crownpickup = None
    self.damagedone = None
    self.headshotrate = None
    self.killgame = None
    self.killmin = None

    self.embed = discord.Embed(title="", color=HyperScapeColor)

    self.HTMLCrawling(playerNickname)

  def HTMLCrawling(self, playerNickname):
    try:
      self.error = self.soup.find('h1').get_text()
    except AttributeError as e:
      self.error = 'none'

    if playerNickname == 'apple19760401':
      self.embed = discord.Embed(title="개발자의 전적은 비밀입니다 ㅎㅎ", color=ErrorColor)
      self.embed.add_field(name="플레이어 정보를 찾지 못함", value="닉네임 오류!", inline=True)
      self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
      self.embed.set_footer(text="Bot made by. 빨강고양이#5278", icon_url=delvoperIcon)

    elif self.error == '404':
      self.embed = discord.Embed(title="error", color=ErrorColor)
      self.embed.add_field(name="플레이어 정보를 찾지 못함", value="명령어, 닉네임이 정확한지 다시 한번 확인해주세요", inline=True)
      self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
      self.embed.set_footer(text="Bot made by. 빨강고양이#5278", icon_url=delvoperIcon)

    else:
      for x in range(0, 16):
        if x == 0:
          self.kda = self.soup.select(".value")[x].get_text()
        elif x == 1:
          self.wins = self.soup.select(".value")[x].get_text()
        elif x == 2:
          self.winrate = self.soup.select(".value")[x].get_text()
        elif x == 3:
          self.avgservivaltime = self.soup.select(".value")[x].get_text()
        elif x == 4:
          self.crownrate = self.soup.select(".value")[x].get_text()
        elif x == 5:
          self.crownwins = self.soup.select(".value")[x].get_text()
        elif x == 6:
          self.kills = self.soup.select(".value")[x].get_text()
        elif x == 7:
          self.assists = self.soup.select(".value")[x].get_text()
        elif x == 8:
          self.chests = self.soup.select(".value")[x].get_text()
        elif x == 9:
          self.fusions = self.soup.select(".value")[x].get_text()
        elif x == 10:
          self.revives = self.soup.select(".value")[x].get_text()
        elif x == 11:
          self.crownpickup = self.soup.select(".value")[x].get_text()
        elif x == 12:
          self.damagedone = self.soup.select(".value")[x].get_text()
        elif x == 13:
          self.headshotrate = self.soup.select(".value")[x].get_text()
        elif x == 14:
          self.killgame = self.soup.select(".value")[x].get_text()
        elif x == 15:
          self.killmin = self.soup.select(".value")[x].get_text()
        playtime = self.soup.find('span', {'class': 'playtime'}).get_text()
        playtime = playtime[11:-19]
        matches = self.soup.find('span', {'class': 'matches'}).get_text()
        matches = matches[11:-17]
        rank = self.soup.select(".rank")[0].get_text()
        rank = rank[19:]

        self.embed = discord.Embed(title=playerNickname + "님의 전적 (" + self.platform + ")", color=HyperScapeColor)
        self.embed.add_field(name="플레이타임", value=playtime, inline=True)
        self.embed.add_field(name="게임 수", value=matches+'게임', inline=True)
        self.embed.add_field(name="K/d", value=self.kda, inline=True)
        self.embed.add_field(name="승리", value=str(self.wins) + '게임', inline=True)
        self.embed.add_field(name="승리 비율", value=self.winrate, inline=True)
        self.embed.add_field(name="평균 생존 시간", value=self.avgservivaltime, inline=True)
        self.embed.add_field(name="왕관 획득", value=str(self.crownrate) + '%', inline=True)
        self.embed.add_field(name="왕관으로 이긴 게임", value=str(self.crownwins) + '게임', inline=True)
        self.embed.add_field(name="킬", value=str(self.kills) + '킬', inline=True)
        self.embed.add_field(name="어시스트", value=self.assists, inline=True)
        self.embed.add_field(name="파괴한 보급품", value=str(self.chests) + '개', inline=True)
        self.embed.add_field(name="합성된 아이템 수", value=str(self.fusions) + '개', inline=True)
        self.embed.add_field(name="부활", value=str(self.revives) + '회', inline=True)
        self.embed.add_field(name="왕관 획득 수", value=str(self.crownpickup) + '번', inline=True)
        self.embed.add_field(name="총합 데미지", value=str(self.damagedone), inline=True)
        self.embed.add_field(name="헤드샷 비율", value=self.headshotrate, inline=True)
        self.embed.add_field(name="게임당 킬수", value=str(self.killgame) + '킬', inline=True)
        self.embed.add_field(name="분당 킬수", value=str(self.killmin) + '킬', inline=True)
        self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        self.embed.set_footer(text="Bot made by. 빨강고양이#5278", icon_url=delvoperIcon)


class HyperScapeRecordSearchPC(HyperScapeRecordSearch):
  platformLink = "uplay/"
  platform = "PC"

class HyperScapeRecordSearchPS4(HyperScapeRecordSearch):
  platformLink = "psn/"
  platform = "PS4"

class HyperScapeRecordSearchXBOX(HyperScapeRecordSearch):
  platformLink = "xbl/"
  platform = "XBOX"
