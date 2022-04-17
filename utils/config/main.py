from datetime import datetime, timedelta

class Time:
  def get_time_today():
    date = datetime.today()
    today = date.strftime('%y%m%d')
    return today


  def get_time_tomorrow():
    date = datetime.today() + timedelta(1)
    tomorrow = date.strftime('%y%m%d')
    return tomorrow


  def get_time():
    a = datetime.today()
    date = str(a.strftime('%y-%m-%d %H:%M:%S'))
    return date


class ColorPalette:
  main_color = 0x2EFEF7
  error_color = 0xFF0000
  hyperScape_color = 0x9ED7D0
  overwatch_color = 0xF89E1B
  league_of_legend_color = 0x5CD1E5


class Config:
  footer_msg = 'Bot made by. 빨강고양이#5278'