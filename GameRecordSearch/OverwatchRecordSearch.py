import requests
import discord

import config

errorColor = config.Config.Error_Color
OverwatchColor = config.Config.OverwatchColor

class ProfileSearch:
    def __init__(self, battleTag):
        playerNickname = battleTag.replace('#', '-', 1)

        self.battleTag = battleTag

        self.url = "https://owapi.io/profile/pc/kr/" + playerNickname

        self.r = requests.get(self.url)
        self.j = self.r.json()

        try:
            self.profileImg = self.j['portrait']

            self.userName = self.j['username']
            self.userLevel = self.j['level']
            self.sportManShip = self.j['endorsement']['sportsmanship']['rate']
            self.shotCaller = self.j['endorsement']['shotcaller']['rate']
            self.teamMate = self.j['endorsement']['teammate']['rate']
            self.recommendationLevel = self.j['endorsement']['level']
            self.profile = self.j['private']

            if not self.profile:
                self.quickplayWin = self.j['games']['quickplay']['won']
                self.quickplayPlayed = self.j['games']['quickplay']['played']
                self.competitiveWin = self.j['games']['competitive']['won']
                self.competitiveLost = self.j['games']['competitive']['lost']
                self.competitiveDraw = self.j['games']['competitive']['draw']
                self.competitivePlayed = self.j['games']['competitive']['played']
                self.competitiveWin_rate = self.j['games']['competitive']['win_rate']
                self.quickplayPlayTime = self.j['playtime']['quickplay']
                self.competitivePlayTime = self.j['playtime']['competitive']

                self.tank = self.j['competitive']['tank']['rank']
                self.dps = self.j['competitive']['damage']['rank']
                self.support = self.j['competitive']['support']['rank']

            self.embed = discord.Embed(title=self.userName + "의 전적", desciprion="LV " + str(self.userLevel),
                                       color=OverwatchColor)
            self.embed.set_thumbnail(url=self.profileImg)

            self.parseJson()
        except:
            print('Error: Not Found User => ' + self.battleTag)
            self.commandError()

    def commandError(self):
        self.embed = discord.Embed(title='Search Error', color=errorColor)
        self.embed.add_field(name='배틀 태그: ' + self.battleTag, value='입력하신 배틀 태그가 잘못 되었습니다.\n확인 후 다시 입력해주시길 바랍니다.')

    def parseJson(self):
        self.embed.add_field(name='추천 레벨: ' + str(self.recommendationLevel),
                             value='스포츠 정신: ' + str(self.sportManShip) + '%\n' + '지휘관: ' + str(
                                 self.shotCaller) + '%\n' + '팀 플레이어: ' + str(self.teamMate) + '%', inline=False)
        if not self.profile:
            self.embed.add_field(name='빠른 대전',
                                 value='승리: ' + str(self.quickplayWin) + '판\n' + '플레이 수: ' + str(
                                     self.quickplayPlayed) + '판\n' + '플레이 시간' + str(self.quickplayPlayTime),
                                 inline=False)
            self.embed.add_field(name='경쟁전',
                                 value='승리: ' + str(self.competitiveWin) + "판\n" + "패배: " + 
                                       str(self.competitiveLost) + "판\n" + "무승부: " + 
                                       str(self.competitiveDraw) + "판\n" + "플레이 판 수: " + 
                                       str(self.competitivePlayed) + "판\n" + "승률: " + 
                                       str(self.competitiveWin_rate) + "%\n" + "플레이 시간" + str(self.competitivePlayTime),
                                 inline=False)
            self.embed.add_field(name='경쟁전 점수',
                                 value='탱커: ' + str(self.tank) + '점\n' + '딜러: ' + str(self.dps) + '점\n' + '힐러: ' + 
                                       str(self.support) + '점\n')

class StatsSearch:
    Game = '빠른대전 or 경쟁전'

    def __init__(self, battleTag):
        playerNickname = battleTag.replace('#', '-', 1)
        self.url = "https://owapi.io/stats/pc/kr/" + playerNickname

        self.r = requests.get(self.url)
        self.j = self.r.json()

        self.userName = self.j['username']
        self.level = self.j['level']
        self.userImg = self.j['portrait']

        self.embed = discord.Embed(title=self.Game + ' 스텟', description="LV " + str(self.level), color=OverwatchColor)
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

            for i in range(0, 3):
                # 많이 플레이한 상위 3개 영웅 이름과 플레이 시간
                self.quickPlayedHero[i] = self.j['stats']['top_heroes']['quickplay']['played'][i]['hero']
                self.quickPlayedTime[i] = self.j['stats']['top_heroes']['quickplay']['played'][i]['played']

                # 승리한 판이 많은 상위 3개 영웅 이름과 승리한 판 수
                self.quickWonHero[i] = self.j['stats']['top_heroes']['quickplay']['games_won'][i]['hero']
                self.quickWonGames[i] = self.j['stats']['top_heroes']['quickplay']['games_won'][i]['games_won']

                # 명중률이 높은 상위 3개 영웅과 명중률
                self.quickWeapon_accuracyHero[i] = self.j['stats']['top_heroes']['quickplay']['weapon_accuracy'][i]['hero']
                self.quickWeapon_accuracy[i] = self.j['stats']['top_heroes']['quickplay']['weapon_accuracy'][i]['weapon_accuracy']

            # Game play stats
            self.allDamage = self.j['stats']['combat']['quickplay'][0]['value']  # 준 피해
            self.barrierDamage = self.j['stats']['combat']['quickplay'][1]['value']  # 방벽에 준 피해
            self.deaths = self.j['stats']['combat']['quickplay'][3]['value']  # 데스
            self.kill = self.j['stats']['combat']['quickplay'][4]['value']  # 킬
            self.heroDamage = self.j['stats']['combat']['quickplay'][6]['value']  # 영웅에게 준 피해
            self.healing = self.j['stats']['assists']['quickplay'][1]['value']  # 치유량

            # Game play stats (average)
            self.averageAllDamage = self.j['stats']['average']['quickplay'][0]['value']  # 준 피해 - 10분 당
            self.averageBarrierDamage = self.j['stats']['average']['quickplay'][1]['value']  # 방벽에 준 피해 - 10분 당
            self.averageKill = self.j['stats']['average']['quickplay'][3]['value']  # 킬 - 10분 당
            self.averageHealing = self.j['stats']['average']['quickplay'][5]['value']  # 치유 - 10분 당
            self.averageHeroDamage = self.j['stats']['average']['quickplay'][6]['value']  # 영웅에게 준 피해 - 10분 당

            # Game play stats (best)
            self.bestAllDamage = self.j['stats']['best']['quickplay'][0]['value']  # 준 피해 - 한 게임 최고기록
            self.bestBarrierDamage = self.j['stats']['best']['quickplay'][1]['value']  # 방벽에 준 피해량 - 한 게임 최고 기록
            self.bestKill = self.j['stats']['best']['quickplay'][3]['value']  # 킬 - 한 게임 최고 기록
            self.bestHealing = self.j['stats']['best']['quickplay'][6]['value']  # 치유량 - 한 게임 최고 기록
            self.bestHeroDamage = self.j['stats']['best']['quickplay'][7]['value']  # 영웅에게 준 피해 - 한 게임 최고 기록

            self.quickParseJson()

        elif self.Game == '경쟁전':
            self.competitivePlayedHero = [1, 2, 3]
            self.competitivePlayedTime = [1, 2, 3]
            self.competitiveWin_rateHero = [1, 2, 3]
            self.competitiveWin_rateGames = [1, 2, 3]
            self.competitiveWeapon_accuracyHero = [1, 2, 3]
            self.competitiveWeapon_accuracy = [1, 2, 3]
            self.competitiveKDAHero = [1, 2, 3]
            self.competitiveKDA = [1, 2, 3]

            for i in range (0, 3):
                self.competitivePlayedHero[i] = self.j['stats']['top_heroes']['competitive']['played'][i]['hero']
                self.competitivePlayedTime[i] = self.j['stats']['top_heroes']['competitive']['played'][i]['played']
                self.competitiveWin_rateHero[i] = self.j['stats']['top_heroes']['competitive']['win_rate'][i]['hero']
                self.competitiveWin_rateGames[i] = self.j['stats']['top_heroes']['competitive']['win_rate'][i]['win_rate']
                self.competitiveWeapon_accuracyHero[i] = self.j['stats']['top_heroes']['competitive']['weapon_accuracy'][i]['hero']
                self.competitiveWeapon_accuracy[i] = self.j['stats']['top_heroes']['competitive']['weapon_accuracy'][i]['weapon_accuracy']
                self.competitiveKDAHero[i] = self.j['stats']['top_heroes']['competitive']['eliminations_per_life'][i]['hero']
                self.competitiveKDA[i] = self.j['stats']['top_heroes']['competitive']['eliminations_per_life'][i]['eliminations_per_life']

            # Game play stats
            self.allDamage = self.j['stats']['combat']['competitive'][0]['value']  # 준 피해
            self.barrierDamage = self.j['stats']['combat']['competitive'][1]['value']  # 방벽에 준 피해
            self.deaths = self.j['stats']['combat']['competitive'][3]['value']  # 데스
            self.kill = self.j['stats']['combat']['competitive'][4]['value']  # 킬
            self.heroDamage = self.j['stats']['combat']['competitive'][7]['value']  # 영웅에게 준 피해
            self.healing = self.j['stats']['assists']['competitive'][1]['value']  # 치유량

            # Game play stats (average)
            self.averageAllDamage = self.j['stats']['average']['competitive'][0]['value']  # 모든 피해 - 10분 당
            self.averageBarrierDamage = self.j['stats']['average']['competitive'][1]['value']  # 방벽에 준 피해 - 10분 당
            self.averageKill = self.j['stats']['average']['competitive'][3]['value']  # 킬 - 10분 당
            self.averageHealing = self.j['stats']['average']['competitive'][5]['value']  # 치유 - 10분 당
            self.averageHeroDamage = self.j['stats']['average']['competitive'][6]['value']  # 영웅에게 준 피해 - 10분 당

            # Game play stats (best)
            self.bestAllDamage = self.j['stats']['best']['competitive'][0]['value']  # 준 피해 - 한 게임 최고기록
            self.bestBarrierDamage = self.j['stats']['best']['competitive'][1]['value']  # 방벽에 준 피해량 - 한 게임 최고 기록
            self.bestKill = self.j['stats']['best']['competitive'][3]['value']  # 킬 - 한 게임 최고 기록
            self.bestHealing = self.j['stats']['best']['competitive'][5]['value']  # 치유량 - 한 게임 최고 기록
            self.bestHeroDamage = self.j['stats']['best']['competitive'][6]['value']  # 영웅에게 준 피해 - 한 게임 최고 기록

            self.competitiveParseJson()

    def quickParseJson(self):
        for i in range (0, 3):
            self.embed.add_field(name="플레이 시간 top " + str(i + 1), value=self.quickPlayedHero[i] + ": " + str(self.quickPlayedTime[i]), inline=True)

        for i in range (0, 3):
            self.embed.add_field(name="승리한 판 top " + str(i + 1), value=self.quickWonHero[i] + ": " + str(self.quickWonGames[i]) + "판", inline=True)

        for i in range(0, 3):
            self.embed.add_field(name="명중률 top " + str(i + 1), value=self.quickWeapon_accuracyHero[i] + ": " + str(self.quickWeapon_accuracy[i]), inline=True)

        self.embed.add_field(name="킬", value=str(self.kill) + "킬", inline=True)
        self.embed.add_field(name="데스", value=str(self.deaths) + "데스", inline=True)
        self.embed.add_field(name="준 피해", value=str(self.allDamage) + "딜", inline=True)
        self.embed.add_field(name="방벽에 준 피해", value=str(self.barrierDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해", value=str(self.heroDamage) + "딜", inline=True)
        self.embed.add_field(name="치유량", value=str(self.healing) + "힐", inline=True)

        self.embed.add_field(name="킬 - 10분 당", value=str(self.averageKill) + "킬", inline=True)
        self.embed.add_field(name="치유량 - 10분 당", value=str(self.averageHealing) + "힐", inline=True)
        self.embed.add_field(name="준 피해 - 10분 당", value=str(self.averageAllDamage) + "딜", inline=True)
        self.embed.add_field(name="방벽에 준 피해 - 10분 당", value=str(self.averageBarrierDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해 - 10분 당", value=str(self.averageHeroDamage) + "딜", inline=True)

        self.embed.add_field(name="킬 - 한 게임 최고 기록", value=str(self.bestKill) + "킬", inline=True)
        self.embed.add_field(name="치유량 - 한 게임 최고 기록", value=str(self.bestHealing) + "힐", inline=True)
        self.embed.add_field(name="준 피해 - 한 게임 최고 기록", value=str(self.bestAllDamage) + "딜", inline=True)
        self.embed.add_field(name="방벽에 준 피해 - 한 게임 최고 기록", value=str(self.bestBarrierDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해 - 한 게임 최고 기록", value=str(self.bestHeroDamage) + "딜", inline=True)

    def competitiveParseJson(self):
        for i in range(0, 3):
            self.embed.add_field(name="플레이 시간 top " + str(i + 1), value=self.competitivePlayedHero[i] + ": " + str(self.competitivePlayedTime[i]), inline=True)

        for i in range(0, 3):
            self.embed.add_field(name="승률 top " + str(i + 1), value=self.competitiveWin_rateHero[i] + ": " + str(self.competitiveWin_rateGames[i]), inline=True)

        for i in range(0, 3):
            self.embed.add_field(name="K/DA top " + str(i + 1), value=self.competitiveKDAHero[i] + ": " + str(self.competitiveKDA[i]), inline=True)

        for i in range(0, 3):
            self.embed.add_field(name="명중률 top " + str(i + 1), value=self.competitiveWeapon_accuracyHero[i] + ": " + str(self.competitiveWeapon_accuracy[i]), inline=True)

        self.embed.add_field(name="킬", value=str(self.kill) + "킬", inline=True)
        self.embed.add_field(name="데스", value=str(self.deaths) + "데스", inline=True)
        self.embed.add_field(name="치유량", value=str(self.healing) + "힐", inline=True)
        self.embed.add_field(name="준 피해", value=str(self.allDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해", value=str(self.heroDamage) + "딜", inline=True)

        self.embed.add_field(name="킬 - 10분 당", value=str(self.averageKill) + "킬", inline=True)
        self.embed.add_field(name="치유량 - 10분 당", value=str(self.averageHealing) + "힐", inline=True)
        self.embed.add_field(name="준 피해 - 10분 당", value=str(self.averageAllDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해 - 10분 당", value=str(self.averageHeroDamage) + "딜", inline=True)

        self.embed.add_field(name="킬 - 한 게임 최고 기록", value=str(self.bestKill) + "킬", inline=True)
        self.embed.add_field(name="치유량 - 한 게임 최고 기록", value=str(self.bestHealing) + "힐", inline=True)
        self.embed.add_field(name="준 피해 - 한 게임 최고 기록", value=str(self.bestAllDamage) + "딜", inline=True)
        self.embed.add_field(name="영웅에게 준 피해 - 한 게임 최고 기록", value=str(self.bestHeroDamage) + "딜", inline=True)

class quick(StatsSearch):
    Game = '빠른대전'

class competitive(StatsSearch):
    Game = '경쟁전'