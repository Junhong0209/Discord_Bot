from datetime import datetime, timedelta

class Config:
    token = "NzkzMDg1OTUyMjU0ODAzOTg4.X-nI2Q.QsGUVKfupP8VnHxBfxZ-4IdAEzw"

    Color = 0x2EFEF7               # 이 봇의 기본 임베드 색상
    HyperScape_Color = 0x9ed7d0    # 핲스 전적 검색 임베드 색상
    Error_Color = 0xff0000         # 명령어 및 오류 임베드 색상

    date = datetime.today()                  # 오늘 날짜 받아오기 (yyyy-mm-dd HH:mm:ss)
    date2 = datetime.today() + timedelta(1)  # 내일 날짜 받아오기 (yyyy-mm-dd HH:mm:ss)
    today = date.strftime('%y%m%d')          # date를 yyyymmdd 형태로 바꾸어줌
    tomorrow = date2.strftime('%y%m%d')      # date2 yyyymmdd 형태로 바꾸어줌