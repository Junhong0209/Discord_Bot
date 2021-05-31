import requests
import discord

import config

OverwatchColor = config.Config.OverwatchColor

class OverwatchRecordSearch:
    def __init__(self, battleTag):
        playerNickname = battleTag.replace('#', '-', 1)

        self.url = "https://best-overwatch-api.herokuapp.com/player/pc/kr/" + playerNickname

        self.BattleTag = battleTag

        self.r = requests.get(self.url)
        self.j = self.r.json()
        
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
            self.competitiveRank = self.j['competitive']['rank']
            self.competitiveRank_img = self.j['competitive']['rank_img']

        self.embed = discord.Embed(title=self.userName + "의 전적", description="LV " + str(self.userLevel), color=OverwatchColor)
        self.embed.set_thumbnail(url=self.profileImg)

        self.parseJson()

    def parseJson(self):
        self.embed.add_field(name='추천 레벨: ' + str(self.recommendationLevel), value='스포츠 정신: ' + str(self.sportManShip) + "%\n" + '지휘관: ' + str(self.shotCaller) + '%\n' + '팀 플레이어: ' + str(self.teamMate) + '%', inline=False)
        if not self.profile:
            self.embed.add_field(name='프로필 상태', value='현재 프로필 공개 상태입니다.', inline=False)
            self.embed.add_field(name='빠른대전', value="승리: " + str(self.quickplayWin) + "판\n" + "플레이 판 수: " + str(self.quickplayPlayed) + "판\n" + "플레이 시간: " + self.quickplayPlayTime, inline=False)
            if self.competitiveWin is not None:
                self.embed.add_field(name='경쟁전', value='승리: ' + str(self.competitiveWin) + "판\n" + "패배: " + str(self.competitiveLost) + "판\n" + "무승부: " + str(self.competitiveDraw) + "판\n" + "플레이 판 수: " + str(self.competitivePlayed) + "판\n" + "승률: " + str(self.competitiveWin_rate) + "%" + "플레이 시간" + str(self.competitivePlayTime), inline=False)
            else:
                self.embed.add_field(name='경쟁전', value='경쟁전을 플레이 하지 않아서 전적이 존재 하지 않습니다.')
        else:
            self.embed.add_field(name='프로필 상태', value='현재 프로필 비공개 상태입니다.\n프로필을 확인할 수 없습니다.', inline=False)