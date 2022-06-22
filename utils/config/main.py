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


class BS4:
  Protocol = 'https://'
  Headers = ''
  Cookies = ''


class Config:
  footer_msg = 'Bot made by. 빨강고양이#5278'