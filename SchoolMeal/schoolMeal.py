########## 외부 라이브러리 ##########
import requests
import discord

########## 다른 파이썬 파일 ##########
import config
import Image.Image

image = Image.Image

########### Embed Color ##########
Color = config.Config.Color
ErrorColor = config.Config.ErrorColor

########### Image ###########
developerImg = image.icon

def Error():
  embed = discord.Embed(title='Error', color=ErrorColor)
  embed.add_field(name='존재하지 않는 명령어입니다.', value='명령어를 확인 후 다시 입력해 주세요.')
  embed.set_footer(text='made by. 빨강고양이#5278', icon_url=developerImg)
  return embed

# 학교 정보
def schoolInformation(educationOffice, schoolCode, time):
  information = {
    'Type': 'json',
    'ATPT_OFCDC_SC_CODE': educationOffice,  # 시도교육청코드
    'SD_SCHUL_CODE': schoolCode,            # 표준학교코드
    'MLSV_YMD': time                         # 급식일자
  }
  return information

class getSchoolMeal:
  date = '오늘 or 내일'

  def __init__(self, params, logo, schoolName):
    self.thumbnail = logo
    self.url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    self.icon = developerImg

    self.embed = discord.Embed(title=schoolName + ' 급식 (' + self.date + ')', color=Color)
    self.embed.set_thumbnail(url=self.thumbnail)

    self.r = requests.get(self.url, params=params)
    self.j = self.r.json()

    self.parseJson()

  def parseJson(self):
    try:
      for menu in self.j['mealServiceDietInfo'][1]['row']:
        self.embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)
        self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=self.icon)

    except KeyError:
      self.embed = discord.Embed(title=self.date + "의 급식", color=ErrorColor)
      self.embed.add_field(name=self.date + '은 급식이 없습니다.', value=self.date + '은 주말 or 공휴일 이므로 급식이 없습니다.')
      self.embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=self.icon)

class getMeal_today(getSchoolMeal):
  date = '오늘'

class getMeal_tomorrow(getSchoolMeal):
  date = '내일'
