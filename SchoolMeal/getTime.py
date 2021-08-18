from datetime import datetime, timedelta

def get_time_today():
  date = datetime.today()                   # 오늘 날짜 받아오기 (yyyy-mm-dd HH:mm:ss)
  today = date.strftime("%y%m%d")           # date를 yyyymmdd 형태로 바꾸어줌
  return today

def get_time_tomorrow():
  date = datetime.today() + timedelta(1)    # 내일 날짜 받아오기 (yyyy-mm-dd HH:mm:ss)
  tomorrow = date.strftime('%y%m%d')        # date를 yyyymmdd 형태로 바꾸어줌
  return tomorrow