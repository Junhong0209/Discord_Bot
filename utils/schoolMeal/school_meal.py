import re

import discord
import requests

from utils.config.main import Config, ColorPalette
from utils.image.main import Image

dev_icon = Image.icon
color = ColorPalette.main_color
error_color = ColorPalette.error_color
msg = Config.footer_msg


def school_information(education_office, school_code, time):
  information = {
    'Type': 'json',
    'ATPT_OFCDC_SC_CODE': education_office,  # 시도교육청코드
    'SD_SCHUL_CODE': school_code,            # 표준학교코드
    'MLSV_YMD': time                         # 급식일자
  }
  
  return information


class GetSchoolMeal:
  date = '오늘이나 내일'

  def __init__(self, params, logo, school_name):
    self.thumbnail = logo
    self.url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    self.icon = dev_icon
    
    self.embed = discord.Embed(title=f'{school_name} 급식 ({self.date})', color=color)
    self.embed.set_thumbnail(url=self.thumbnail)
    
    self.request = requests.get(self.url, params)
    self.json = self.request.json()
    
    self.parse_json()
    
  def parse_json(self):
    try:
      for menu in self.json['mealServiceDietInfo'][1]['row']:
        self.embed.add_field(name=menu['MMEAL_SC_NM'], value=re.sub(r'[0-9]+.', '', menu['DDISH_NM'].replace('<br/>', '\n')), inline=True)
        self.embed.set_footer(text=msg, icon_url=self.icon)
    except KeyError:
      self.embed = discord.Embed(title=f'{self.date}의 급식', color=error_color)
      self.embed.add_field(name=f'{self.date}은 급식이 없습니다.', value=f'{self.date}은(는) 주말 또는 공휴일 이므로 급식이 없습니다.')
      self.embed.set_footer(text=msg, icon_url=dev_icon)


class GetMealToday(GetSchoolMeal):
  date = '오늘'


class GetMealTomorrow(GetSchoolMeal):
  date = '내일'
