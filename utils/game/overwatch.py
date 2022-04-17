import discord
import requests

from utils.image.main import Image
from utils.config.main import ColorPalette

icon = Image.icon
error_color = ColorPalette.error_color
overwatch_color = ColorPalette.overwatch_color


class ProfileSearch:
  def __init__(self, battle_tag):
    self.playerNickname = battle_tag.replace('#', '-', 1)
    
    self.battleTag = battle_tag
    
    self.chkPlace = self.playerNickname.split('-')
    
    if self.chkPlace[1].startswith('1'):
      self.url = f"https://owapi.io/profile/pc/us/{self.playerNickname}"
    elif self.chkPlace[1].startswith('2'):
      self.url = f"https://owapi.io/profile/pc/eu/{self.playerNickname}"
    elif self.chkPlace[1].startswith('3'):
      self.url = f"https://owapi.io/profile/pc/kr/{self.playerNickname}"
    elif self.chkPlace[1].startswith('4'):
      self.url = f"https://owapi.io/profile/pc/global/{self.playerNickname}"
    elif self.chkPlace[1].startswith('5'):
      self.url = f"https://owapi.io/profile/pc/cn/{self.playerNickname}"
    
    self.request = requests.get(self.url)
    self.json = self.request.json()
    
    try:
      self.profileImg = self.json['portrait']
      
      self.userName = self.json['username']
      self.userLevel = self.json['level']
      self.sportManShip = self.json['endorsement']['sportsmanship']['rate']
      self.shotCaller = self.json['endorsement']['shotcaller']['rate']
      self.teamMate = self.json['endorsement']['teammate']['rate']
      self.recommendationLevel = self.json['endorsement']['level']
      self.profile = self.json['private']
      
      if not self.profile:
        self.quickplayWin = self.json['games']['quickplay']['won']
        self.quickplayPlayed = self.json['games']['quickplay']['played']
        self.competitiveWin = self.json['games']['competitive']['won']
        self.competitiveLost = self.json['games']['competitive']['lost']
        self.competitiveDraw = self.json['games']['competitive']['draw']
        self.competitivePlayed = self.json['games']['competitive']['played']
        self.competitiveWin_rate = self.json['games']['competitive']['win_rate']
        self.quickplayPlayTime = self.json['playtime']['quickplay']
        self.competitivePlayTime = self.json['playtime']['competitive']
        
        self.tank = self.json['competitive']['tank']['rank']
        self.dps = self.json['competitive']['damage']['rank']
        self.support = self.json['competitive']['support']['rank']
        
        self.embed = discord.Embed(title=self.userName + "의 전적", desciprion=f"LV {str(self.userLevel)}", color=overwatch_color)
        self.embed.set_thumbnail(url=self.profileImg)
        
        self.parse_json()
    
    except IndexError:
      self.not_found_player_stat()
    
    except:
      print(f'Error: Not Found User => {self.battleTag}')
      self.not_found_user_error()
  
  def not_found_player_stat(self):
    self.embed = discord.Embed(title='Search Error', color=error_color)
    self.embed.add_field(name='경쟁전 스탯을 찾지 못하였습니다.', value='전적이 검색되지 않았습니다.\nNot Found Player Stat.')
  
  def not_found_user_error(self):
    self.embed = discord.Embed(title='Search Error', color=error_color)
    self.embed.add_field(name=f'배틀 태그: {self.battleTag}', value='입력하신 배틀 태그가 잘못 되었습니다.\n확인 후 다시 입력해주시길 바랍니다.')
  
  def parse_json(self):
    self.embed.add_field(name=f'추천 레벨: {str(self.recommendationLevel)}', value=f'스포츠 정신: {str(self.sportManShip)}%\n지휘관: {str(self.shotCaller)}%\n팀 플레이어: {str(self.teamMate)}%', inline=False)
    if not self.profile:
      self.embed.add_field(name='빠른 대전', value=f'승리: {str(self.quickplayWin)}판\n플레이 수: {str(self.quickplayPlayed)}판\n플레이 시간: {str(self.quickplayPlayTime)}', inline=False)
      self.embed.add_field(name='경쟁전', value=f'승리: {str(self.competitiveWin)}판\n패배: {str(self.competitiveLost)}판\n무승부: {str(self.competitiveDraw)}판\n플레이 판 수: {str(self.competitivePlayed)}판\n승률: {str(self.competitiveWin_rate)}%\n플레이 시간: {str(self.competitivePlayTime)}', inline=False)
      self.embed.add_field(name='경쟁전 점수', value=f'탱커: {str(self.tank)}점\n딜러: {str(self.dps)}점\n힐러: {str(self.support)}점\n')
      self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=icon)


class StatsSearch:
  Game = '빠른대전 or 경쟁전'
  
  def __init__(self, battle_tag):
    self.playerNickname = battle_tag.replace('#', '-', 1)
    
    self.battleTag = battle_tag
    
    self.chkPlace = self.playerNickname.split('-')
    
    if self.chkPlace[1].startswith('1'):
      self.url = "https://owapi.io/profile/pc/us/" + self.playerNickname
    elif self.chkPlace[1].startswith('2'):
      self.url = "https://owapi.io/profile/pc/eu/" + self.playerNickname
    elif self.chkPlace[1].startswith('3'):
      self.url = "https://owapi.io/profile/pc/kr/" + self.playerNickname
    elif self.chkPlace[1].startswith('4'):
      self.url = "https://owapi.io/profile/pc/global/" + self.playerNickname
    elif self.chkPlace[1].startswith('5'):
      self.url = "https://owapi.io/profile/pc/cn/" + self.playerNickname
    
    self.request = requests.get(self.url)
    self.json = self.request.json()
    
    self.userName = self.json['username']
    self.level = self.json['level']
    self.userImg = self.json['portrait']
    
    self.embed = discord.Embed(title=self.Game + ' 스텟', description="LV " + str(self.level), color=overwatch_color)
    self.embed.set_thumbnail(url=self.userImg)
    
    if self.Game == '빠른대전':
      # 많이 플레이한 상위 3개 영웅 이름과 플레이 시간
      self.quickPlayedHero = [1, 2, 3]
      self.quickPlayedTime = [1, 2, 3]
      # 승리한 판이 많은 상위 3개 영웅 이름과 승리한 판 수
      self.quickWonHero = [1, 2, 3]
      self.quickWonGames = [1, 2, 3]
      # 명중률이 높은 상위 3개 영웅과 명중률
      self.quickWeapon_accuracyHero = [1, 2, 3]
      self.quickWeapon_accuracy = [1, 2, 3]

      for i in range(3):
        # 많이 플레이한 상위 3개 영웅 이름과 플레이 시간
        self.quickPlayedHero[i] = self.json['stats']['top_heroes']['quickplay']['played'][i]['hero']
        self.quickPlayedTime[i] = self.json['stats']['top_heroes']['quickplay']['played'][i]['played']
        # 승리한 판이 많은 상위 3개 영웅 이름과 승리한 판 수
        self.quickWonHero[i] = self.json['stats']['top_heroes']['quickplay']['games_won'][i]['hero']
        self.quickWonGames[i] = self.json['stats']['top_heroes']['quickplay']['games_won'][i]['games_won']
        # 명중률이 높은 상위 3개 영웅과 명중률
        self.quickWeapon_accuracyHero[i] = self.json['stats']['top_heroes']['quickplay']['weapon_accuracy'][i]['hero']
        self.quickWeapon_accuracy[i] = self.json['stats']['top_heroes']['quickplay']['weapon_accuracy'][i]['weapon_accuracy']

      # Game play stats
      self.allDamage = self.json['stats']['combat']['quickplay'][0]['value']  # 준 피해
      self.barrierDamage = self.json['stats']['combat']['quickplay'][1]['value']  # 방벽에 준 피해
      self.deaths = self.json['stats']['combat']['quickplay'][3]['value']  # 데스
      self.kill = self.json['stats']['combat']['quickplay'][4]['value']  # 킬
      self.heroDamage = self.json['stats']['combat']['quickplay'][6]['value']  # 영웅에게 준 피해
      self.healing = self.json['stats']['assists']['quickplay'][1]['value']  # 치유량
      # Game play stats (average)
      self.averageAllDamage = self.json['stats']['average']['quickplay'][0]['value']  # 준 피해 - 10분 당
      self.averageBarrierDamage = self.json['stats']['average']['quickplay'][1]['value']  # 방벽에 준 피해 - 10분 당
      self.averageKill = self.json['stats']['average']['quickplay'][3]['value']  # 킬 - 10분 당
      self.averageHealing = self.json['stats']['average']['quickplay'][5]['value']  # 치유 - 10분 당
      self.averageHeroDamage = self.json['stats']['average']['quickplay'][6]['value']  # 영웅에게 준 피해 - 10분 당
      # Game play stats (best)
      self.bestAllDamage = self.json['stats']['best']['quickplay'][0]['value']  # 준 피해 - 한 게임 최고기록
      self.bestBarrierDamage = self.json['stats']['best']['quickplay'][1]['value']  # 방벽에 준 피해량 - 한 게임 최고 기록
      self.bestKill = self.json['stats']['best']['quickplay'][3]['value']  # 킬 - 한 게임 최고 기록
      self.bestHealing = self.json['stats']['best']['quickplay'][6]['value']  # 치유량 - 한 게임 최고 기록
      self.bestHeroDamage = self.json['stats']['best']['quickplay'][7]['value']  # 영웅에게 준 피해 - 한 게임 최고 기록

      self.quick_parse_json()

    elif self.Game == '경쟁전':
      self.competitivePlayedHero = [1, 2, 3]
      self.competitivePlayedTime = [1, 2, 3]
      self.competitiveWin_rateHero = [1, 2, 3]
      self.competitiveWin_rateGames = [1, 2, 3]
      self.competitiveWeapon_accuracyHero = [1, 2, 3]
      self.competitiveWeapon_accuracy = [1, 2, 3]
      self.competitiveKDAHero = [1, 2, 3]
      self.competitiveKDA = [1, 2, 3]

      try:
        for i in range(0, 3):
          self.competitivePlayedHero[i] = self.json['stats']['top_heroes']['competitive']['played'][i]['hero']
          self.competitivePlayedTime[i] = self.json['stats']['top_heroes']['competitive']['played'][i]['played']
          self.competitiveWin_rateHero[i] = self.json['stats']['top_heroes']['competitive']['win_rate'][i]['hero']
          self.competitiveWin_rateGames[i] = self.json['stats']['top_heroes']['competitive']['win_rate'][i]['win_rate']
          self.competitiveWeapon_accuracyHero[i] = self.json['stats']['top_heroes']['competitive']['weapon_accuracy'][i][
            'hero']
          self.competitiveWeapon_accuracy[i] = self.json['stats']['top_heroes']['competitive']['weapon_accuracy'][i][
            'weapon_accuracy']
          self.competitiveKDAHero[i] = self.json['stats']['top_heroes']['competitive']['eliminations_per_life'][i]['hero']
          self.competitiveKDA[i] = self.json['stats']['top_heroes']['competitive']['eliminations_per_life'][i][
            'eliminations_per_life']

        # Game play stats
        self.allDamage = self.json['stats']['combat']['competitive'][0]['value']  # 준 피해
        self.barrierDamage = self.json['stats']['combat']['competitive'][1]['value']  # 방벽에 준 피해
        self.deaths = self.json['stats']['combat']['competitive'][3]['value']  # 데스
        self.kill = self.json['stats']['combat']['competitive'][4]['value']  # 킬
        self.heroDamage = self.json['stats']['combat']['competitive'][7]['value']  # 영웅에게 준 피해
        self.healing = self.json['stats']['assists']['competitive'][1]['value']  # 치유량
        # Game play stats (average)
        self.averageAllDamage = self.json['stats']['average']['competitive'][0]['value']  # 모든 피해 - 10분 당
        self.averageBarrierDamage = self.json['stats']['average']['competitive'][1]['value']  # 방벽에 준 피해 - 10분 당
        self.averageKill = self.json['stats']['average']['competitive'][3]['value']  # 킬 - 10분 당
        self.averageHealing = self.json['stats']['average']['competitive'][5]['value']  # 치유 - 10분 당
        self.averageHeroDamage = self.json['stats']['average']['competitive'][6]['value']  # 영웅에게 준 피해 - 10분 당
        # Game play stats (best)
        self.bestAllDamage = self.json['stats']['best']['competitive'][0]['value']  # 준 피해 - 한 게임 최고기록
        self.bestBarrierDamage = self.json['stats']['best']['competitive'][1]['value']  # 방벽에 준 피해량 - 한 게임 최고 기록
        self.bestKill = self.json['stats']['best']['competitive'][3]['value']  # 킬 - 한 게임 최고 기록
        self.bestHealing = self.json['stats']['best']['competitive'][5]['value']  # 치유량 - 한 게임 최고 기록
        self.bestHeroDamage = self.json['stats']['best']['competitive'][6]['value']  # 영웅에게 준 피해 - 한 게임 최고 기록
        
        self.not_found_player_stat()

      except IndexError:
        self.competitive_parse_json()

  def quick_parse_json(self):
    for i in range(0, 3):
      self.embed.add_field(name=f"플레이 시간 top {str(i + 1)}", value=f'{self.quickPlayedHero[i]}: {str(self.quickPlayedTime[i])}', inline=True)

    for i in range(0, 3):
      self.embed.add_field(name=f"승리한 판 top {str(i + 1)}", value=f'{self.quickWonHero[i]}: {str(self.quickWonGames[i])}판', inline=True)

    for i in range(0, 3):
      self.embed.add_field(name=f"명중률 top {str(i + 1)}", value=f'{self.quickWeapon_accuracyHero[i]}: {str(self.quickWeapon_accuracy[i])}', inline=True)

    self.embed.add_field(name="킬", value=f"{str(self.kill)}킬", inline=True)
    self.embed.add_field(name="데스", value=f"{str(self.deaths)}데스", inline=True)
    self.embed.add_field(name="준 피해", value=f"{str(self.allDamage)}딜", inline=True)
    self.embed.add_field(name="방벽에 준 피해", value=f"{str(self.barrierDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해", value=f"{str(self.heroDamage)}딜", inline=True)
    self.embed.add_field(name="치유량", value=f"{str(self.healing)}힐", inline=True)

    self.embed.add_field(name="킬 - 10분 당", value=f"{str(self.averageKill)}킬", inline=True)
    self.embed.add_field(name="치유량 - 10분 당", value=f"{str(self.averageHealing)}힐", inline=True)
    self.embed.add_field(name="준 피해 - 10분 당", value=f"{str(self.averageAllDamage)}딜", inline=True)
    self.embed.add_field(name="방벽에 준 피해 - 10분 당", value=f"{str(self.averageBarrierDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해 - 10분 당", value=f"{str(self.averageHeroDamage)}딜", inline=True)

    self.embed.add_field(name="킬 - 한 게임 최고 기록", value=f"{str(self.bestKill)}킬", inline=True)
    self.embed.add_field(name="치유량 - 한 게임 최고 기록", value=f"{str(self.bestHealing)}힐", inline=True)
    self.embed.add_field(name="준 피해 - 한 게임 최고 기록", value=f"{str(self.bestAllDamage)}딜", inline=True)
    self.embed.add_field(name="방벽에 준 피해 - 한 게임 최고 기록", value=f"{str(self.bestBarrierDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해 - 한 게임 최고 기록", value=f"{str(self.bestHeroDamage)}딜", inline=True)
    self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=icon)

  def not_found_player_stat(self):
    self.embed = discord.Embed(title='Search Error', color=error_color)
    self.embed.add_field(name='경쟁전 스탯을 찾지 못하였습니다.', value='전적이 검색되지 않았습니다.\nNot Found Player Stat.')

  def competitive_parse_json(self):
    for i in range(0, 3):
      self.embed.add_field(name="플레이 시간 top " + str(i + 1), value=f'{self.competitivePlayedHero[i]}: {str(self.competitivePlayedTime[i])}', inline=True)

    for i in range(0, 3):
      self.embed.add_field(name="승률 top " + str(i + 1), value=f'{self.competitiveWin_rateHero[i]}: {str(self.competitiveWin_rateGames[i])}', inline=True)

    for i in range(0, 3):
      self.embed.add_field(name="K/DA top " + str(i + 1), value=f'{self.competitiveKDAHero[i]}: {str(self.competitiveKDA[i])}', inline=True)

    for i in range(0, 3):
      self.embed.add_field(name="명중률 top " + str(i + 1), value=f'{self.competitiveWeapon_accuracyHero[i]}: {str(self.competitiveWeapon_accuracy[i])}', inline=True)

    self.embed.add_field(name="킬", value=f"{str(self.kill)}킬", inline=True)
    self.embed.add_field(name="데스", value=f"{str(self.deaths)}데스", inline=True)
    self.embed.add_field(name="치유량", value=f"{str(self.healing)}힐", inline=True)
    self.embed.add_field(name="준 피해", value=f"{str(self.allDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해", value=f"{str(self.heroDamage)}딜", inline=True)

    self.embed.add_field(name="킬 - 10분 당", value=f"{str(self.averageKill)}킬", inline=True)
    self.embed.add_field(name="치유량 - 10분 당", value=f"{str(self.averageHealing)}힐", inline=True)
    self.embed.add_field(name="준 피해 - 10분 당", value=f"{str(self.averageAllDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해 - 10분 당", value=f"{str(self.averageHeroDamage)}딜", inline=True)

    self.embed.add_field(name="킬 - 한 게임 최고 기록", value=f"{str(self.bestKill)}킬", inline=True)
    self.embed.add_field(name="치유량 - 한 게임 최고 기록", value=f"{str(self.bestHealing)}힐", inline=True)
    self.embed.add_field(name="준 피해 - 한 게임 최고 기록", value=f"{str(self.bestAllDamage)}딜", inline=True)
    self.embed.add_field(name="영웅에게 준 피해 - 한 게임 최고 기록", value=f"{str(self.bestHeroDamage)}딜", inline=True)
    self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=icon)


class Quick(StatsSearch):
  Game = '빠른대전'


class Competitive(StatsSearch):
  Game = '경쟁전'
