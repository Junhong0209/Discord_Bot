import requests
import discord
import config

Color = config.Config.Color
Error_Color = config.Config.Error_Color
HyperScape_Color = config.Config.HyperScape_Color

today = config.Config.today
tomorrow = config.Config.tomorrow

def Error():
    embed = discord.Embed(title="Error", color=Error_Color)
    embed.add_field(name="존재하지 않는 명령어입니다.", value='명령어를 확인 후 다시 입력해 주세요.')
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
    return embed

class get_schoolMeal:
    date = '오늘이나 내일'

    def __init__(self, params, logo, schoolName):
        self.thumbnail = logo
        self.url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        self.icon = 'https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png'

        self.embed = discord.Embed(title=schoolName + ' 급식 (' + self.date + ')', color=Color)
        self.embed.set_thumbnail(url=self.thumbnail)

        self.r = requests.get(self.url, params=params)
        self.j = self.r.json()

        self.parseJson()

    def parseJson(self):
        try:
            for menu in self.j['mealServiceDietInfo'][1]['row']:
                self.embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)
                self.embed.set_footer(text='made by 빨강고양이', icon_url=self.icon)

        except KeyError:
            self.embed = discord.Embed(title=self.date + "의 급식", color=Error_Color)
            self.embed.add_field(name=self.date + '은 급식이 없습니다.', value=self.date + '은 주말 or 공휴일 이므로 급식이 없습니다.')
            self.embed.set_footer(text='made by 빨강고양이', icon_url=self.icon)

class getMeal_Today(get_schoolMeal):
    date = '오늘'

class getMeal_Tomorrow(get_schoolMeal):
    date = '내일'
