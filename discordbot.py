import discord
import asyncio
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import date

token = "NzkzMDg1OTUyMjU0ODAzOTg4.X-nI2Q.QsGUVKfupP8VnHxBfxZ-4IdAEzw"

app = commands.Bot(command_prefix='!')

time = date.today().strftime('%y%m%d') # 시간이 필요한 경우 가져다 사용하면 된다. (출력 방식: yyyymmdd)

#################### 임베드 색상 ####################

Color = 0x2EFEF7                # 이 봇의 기본 임베드 색상
HyperScape_Color = 0x9ed7d0     # 핲스 전적 검색 임베드 색상
Error_Color = 0xff0000          # 명령어 및 오류 임베드 색상

#################### 봇이 켜젔을 때 실행되는 것 ####################

@app.event
async def on_ready():
    print('Loggend-in Bot:', app.user.name)
    print('Bot id:', app.user.id)
    print('connection was succesful')
    print('=' * 30)

    game = discord.Game('정신 차리기')
    await app.change_presence(status=discord.Status.offline, activity=game)
    await asyncio.sleep(5)
    while True:
        game = discord.Game('빡추 스탯 쌓기')
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('여전히 베타 테스트 중이에요~')
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('테스트가 언제 쯤 끝날까요~')
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('!도움말')
        await app.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

#################### 도움말 명령어 ####################

@app.command()
async def 도움말(ctx):
    embed = discord.Embed(title="명령어 모음", description="", colour=Color)
    embed.add_field(name="!안녕", value="봇이 인사를 함", inline=False)
    embed.add_field(name="!빡추 [이름]", value="들어간 이름이 빡추 스탯을 쌓음", inline=False)
    embed.add_field(name="!초대링크", value="봇 초대 링크를 보내줌", inline=False)
    embed.add_field(name="!핲스 도움말", value="하이퍼 스케이프 전적 검색에 사용되는 명령어를 알려준다.", inline=False)
    embed.add_field(name="!씹덕 [이름]", value="말 그대로 씹덕.....", inline=False)
    embed.add_field(name="!급식 도움말", value="급식과 관련된 도움말 알려줌", inline=False)
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
    await ctx.send(embed=embed)

@app.command(aliases=['핲스'])
async def HyperScape_help(ctx, *, text):
    if text == '도움말':
        embed = discord.Embed(title="명령어 사용방법!", color=HyperScape_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="PC용 킬뎃 확인", value="!pc [닉네임]", inline=True)
        embed.add_field(name="PS4용 킬뎃 확인", value="!ps4 [닉네임]", inline=True)
        embed.add_field(name="XBOX용 킬뎃 확인", value="!xbox [닉네임]", inline=True)
        embed.set_footer(text='serviced by hyper scape korea', icon_url='https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684')
        await ctx.send(embed=embed)
    else :
        embed = discord.Embed(title="Error!", color=Error_Color)
        embed.add_field(name="명령어를 찾지 못했습니다.", value="명령어를 제대로 입력하였는지 확인해 주십시요.")
        embed.set_footer(text='serviced by hyper scape korea', icon_url='https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684')
        await ctx.send(embed=embed)

@app.command()
async def 급식(ctx, *, help):
    if help == '도움말':
        embed = discord.Embed(title='급식 도움말', color=Color)
        embed.add_field(name="!대소고 급식", value="대소고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="!문화고 급식", value="문화고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="!예일고 급식", value="예일고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="!신라공고 급식", value="신라공고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="!동성고 급식", value="동성고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="!포철공고 급식", value="포철공고 하루 급식을 보여준다.", inline=False)
        embed.add_field(name="![학교 이름] 급식", value="추후 다른 고등학교 추가 예정", inline=False)
        embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        await ctx.send(embed=embed)

#################### 명령어들 ####################

@app.command()
async def 제작자(ctx): # 자신의 정보를 넣으면 된다.
    embed = discord.Embed(title="제작자 정보", color=Color)
    embed.add_field(name="Discord", value="빨강고양이#5278", inline=False)
    embed.add_field(name="GitHub", value="[제작자의 GitHub](https://github.com/Junhong0209)", inline=False)
    embed.add_field(name="Facebook", value="[제작자의 Facebook](https://www.facebook.com/Junhong04/)", inline=False)
    embed.add_field(name="Instargram", value="[제작자의 Instargram](https://www.instagram.com/junhong936/)", inline=False)
    embed.add_field(name="Blog", value="[제작자의 Blog](https://junhong0209.github.io)", inline=False)
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
    await ctx.send(embed=embed)

@app.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def Hello(ctx):
    await ctx.send('안녕하세요~! {0.author.mention}님. 오늘도 좋은 하루 보내세요!'.format(ctx))

@app.command()
async def 초대링크(ctx):
    embed = discord.Embed(title="봇 초대 링크", description="", color=Color)
    embed.add_field(name="이 봇을 다른 서버에 초대하기 위한 링크입니다.",
                    value="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=793085952254803988&permissions=8&scope=bot)",
                    inline=False)
    await ctx.send(embed=embed)

@app.command()
async def 빡추(ctx, *, text=None):
    if None == text:       # !빡추 명령어 뒤에 아무것도 입력 하지 않은 경우
        await ctx.send("누구를 입력하신거죠? 전 입력 받은게 없습니다만?")
    elif text == "아서":    # !빡추 명령어 뒤에 봇의 이름을 넣은 경우
        await ctx.send("나 빡추 아닌데?")
    else:
        await ctx.send("보셨나요? 보셨나요? 보셨냐구요!!!! " + text + "의 빡추 스탯쌓기!!")
        print(text)

@app.command()
async def 씹덕(ctx, text=None):
    if None == text:       # !씹덕 명령어 뒤에 아무것도 입력 하지 않은 경우
        await ctx.send("누구를 입력하신거죠? 전 입력 받은게 없습니다만?")
    elif text == "아서":    # !씹덕 명령어 뒤에 봇의 이름을 넣은 경우
        await ctx.send("나 씹덕 아닌데?")
    else:
        await ctx.send("아, " + text + " 그 씹덕 샛기?")
        print(text)

#################### 각 학교의 급식 ####################
# 찾아 볼 것:
# 학교별 시도교육청 코드, 표준학교코드 찾기
# 파이썬에서 오늘 날짜 가져오는 방법 찾기

@app.command()
async def 대소고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 대소고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'D10', # 시도교육청코드
            'SD_SCHUL_CODE': '7240454', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']:  # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이',
                                 icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

@app.command()
async def 문화고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 문화고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'R10', # 시도교육청코드
            'SD_SCHUL_CODE': '8750172', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']:  # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이',
                                 icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

@app.command()
async def 예일고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 예일고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'R10', # 시도교육청코드
            'SD_SCHUL_CODE': '8750772', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']:  # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이',
                                 icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

@app.command()
async def 신라공고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 신라공고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'R10', # 시도교육청코드
            'SD_SCHUL_CODE': '8750323', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']:  # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이',
                                 icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

@app.command()
async def 동성고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 동성고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'R10', # 시도교육청코드
            'SD_SCHUL_CODE': '8750542', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']:  # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이',
                                 icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

@app.command()
async def 포철공고(ctx, *, schoolMeal):
    if schoolMeal == '급식': # 만약 포철공고 뒤에 급식이라는 글자가 온다면 아래의 코드를 실행한다.

        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
        params = {
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': 'R10', # 시도교육청코드
            'SD_SCHUL_CODE': '8750337', # 표준학교코드
            'MLSV_YMD': time # 급식일자
        }

        r = requests.get(url, params=params)

        j = r.json()

        embed = discord.Embed(title="오늘의 급식", color=Color)

        total_cal = 0

        if j['mealServiceDietInfo'][1]['row']: # 만약 JSON 파일에 mealServiceDietInfo가 있다면 아래의 코드를 실행
            for menu in j['mealServiceDietInfo'][1]['row']:
                # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
                embed.add_field(name=menu['MMEAL_SC_NM'], value=menu['DDISH_NM'].replace('<br/>', '\n'), inline=True)

                # 전체 칼로리 계산
                cal = menu['CAL_INFO']
                cal = float(cal[0:cal.find(' Kcal')])
                total_cal += cal

                embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
            await ctx.send(embed=embed)

        # elif j['RESULT']:
        #     embed = discord.Embed(title="오늘의 급식", color=Error_Color)
        #     embed.add_field(name='오늘은 급식이 없습니다.', value='오늘은 주말 or 공휴일 이므로 급식이 없습니다.')
        #     embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
        #     await ctx.send(embed=embed)

#################### 가위바위보 게임 ####################

# random.choice를 사용하여 봇이 가위, 바위, 보 중 하나를 랜덤으로 뱉어냄
# 입력값과 봇에서 랜덤으로 나온 값을 비교하여 승패를 알려줌
# 게임 한 판이 끝났을 때 계속 할껀지 물어보기
# 만약 계속 한다고 하면 다시 한번 더 하기
# 하지 않겠다고 할 경우 게임을 끝내기

#################### 핲스 전적 검색 명령어 ####################

@app.command()
async def pc(ctx, *, playerNickname):
    webpage = requests.get('https://tracker.gg/hyper-scape/profile/uplay/' + playerNickname + '/overview')
    html = webpage.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        error = soup.find('h1').get_text()
    except AttributeError as e:
        error = 'none'

    # if (playerNickname == 'Red_cat2020'):
    #     embed = discord.Embed(title="개발자의 전적은 비밀입니다 ㅎㅎ", description="made by 빨강고양이", color=Error_Color)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
    #     embed.add_field(name="플레이어 정보를 찾지 못함", value="닉네임 오류!", inline=True)
    #     embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")

    if (error == '404'):
        embed = discord.Embed(title="error", description="made by 빨강고양이", color=Error_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이어 정보를 찾지 못함", value="명령어, 닉네임이 정확한지 다시 한번 확인해주세요", inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")

    else:
        for x in range(0, 16):
            if x == 0:
                kda = soup.select(".value")[x].get_text()
            elif x == 1:
                wins = soup.select(".value")[x].get_text()
            elif x == 2:
                winper = soup.select(".value")[x].get_text()
            elif x == 3:
                avgservivaltime = soup.select(".value")[x].get_text()
            elif x == 4:
                crownper = soup.select(".value")[x].get_text()
            elif x == 5:
                crownwins = soup.select(".value")[x].get_text()
            elif x == 6:
                kills = soup.select(".value")[x].get_text()
            elif x == 7:
                assists = soup.select(".value")[x].get_text()
            elif x == 8:
                chests = soup.select(".value")[x].get_text()
            elif x == 9:
                fusions = soup.select(".value")[x].get_text()
            elif x == 10:
                revives = soup.select(".value")[x].get_text()
            elif x == 11:
                crownpickup = soup.select(".value")[x].get_text()
            elif x == 12:
                damagedone = soup.select(".value")[x].get_text()
            elif x == 13:
                headshotper = soup.select(".value")[x].get_text()
            elif x == 14:
                killgame = soup.select(".value")[x].get_text()
            elif x == 15:
                killmin = soup.select(".value")[x].get_text()
        playtime = soup.find('span', {'class': 'playtime'}).get_text()
        playtime = playtime[11:-19]
        matches = soup.find('span', {'class': 'matches'}).get_text()
        matches = matches[11:-17]
        rank = soup.select(".rank")[0].get_text()
        rank = rank[19:]

        embed = discord.Embed(title=playerNickname + "님의 전적 (PC)", description="made by 빨강고양이", color=HyperScape_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이타임", value=playtime, inline=True)
        embed.add_field(name="게임 수", value=matches + '게임', inline=True)
        embed.add_field(name="K/d", value=kda, inline=True)
        embed.add_field(name="승리", value=wins + '게임', inline=True)
        embed.add_field(name="승리 비율", value=winper, inline=True)
        embed.add_field(name="평균 생존 시간", value=avgservivaltime, inline=True)
        embed.add_field(name="왕관 획득", value=crownper + '%', inline=True)
        embed.add_field(name="왕관으로 이긴 게임", value=crownwins + '게임', inline=True)
        embed.add_field(name="킬", value=kills + '킬', inline=True)
        embed.add_field(name="어시스트", value=assists, inline=True)
        embed.add_field(name="파괴한 보급품", value=chests + '개', inline=True)
        embed.add_field(name="합성된 아이템 수", value=fusions + '개', inline=True)
        embed.add_field(name="부활", value=revives + '회', inline=True)
        embed.add_field(name="왕관 획득 수", value=crownpickup + '번', inline=True)
        embed.add_field(name="총합 데미지", value=damagedone, inline=True)
        embed.add_field(name="헤드샷 비율", value=headshotper, inline=True)
        embed.add_field(name="게임당 킬수", value=killgame + '킬', inline=True)
        embed.add_field(name="분당 킬수", value=killmin + '킬', inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")
    await ctx.send(embed=embed)
    print(playerNickname)

@app.command()
async def ps4(ctx, *, playerNickname):
    webpage = requests.get('https://tracker.gg/hyper-scape/profile/psn/' + playerNickname + '/overview')
    html = webpage.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        error = soup.find('h1').get_text()
    except AttributeError as e:
        error = 'none'

    # if (playerNickname == 'Red_cat2020'):
    #     embed = discord.Embed(title="개발자의 전적은 비밀입니다 ㅎㅎ", description="made by 빨강고양이", color=Error_Color)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
    #     embed.add_field(name="플레이어 정보를 찾지 못함!ps4 a", value="닉네임 오류!", inline=True)
    #     embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")

    if (error == '404'):
        print('Error!')
        embed = discord.Embed(title="error", description="made by 빨강고양이", color=Error_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이어 정보를 찾지 못함", value="명령어, 닉네임이 정확한지 다시 한번 확인해주세요", inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")\

    else:
        for x in range(0, 16):
            if x == 0:
                kda = soup.select(".value")[x].get_text()
            elif x == 1:
                wins = soup.select(".value")[x].get_text()
            elif x == 2:
                winper = soup.select(".value")[x].get_text()
            elif x == 3:
                avgservivaltime = soup.select(".value")[x].get_text()
            elif x == 4:
                crownper = soup.select(".value")[x].get_text()
            elif x == 5:
                crownwins = soup.select(".value")[x].get_text()
            elif x == 6:
                kills = soup.select(".value")[x].get_text()
            elif x == 7:
                assists = soup.select(".value")[x].get_text()
            elif x == 8:
                chests = soup.select(".value")[x].get_text()
            elif x == 9:
                fusions = soup.select(".value")[x].get_text()
            elif x == 10:
                revives = soup.select(".value")[x].get_text()
            elif x == 11:
                crownpickup = soup.select(".value")[x].get_text()
            elif x == 12:
                damagedone = soup.select(".value")[x].get_text()
            elif x == 13:
                headshotper = soup.select(".value")[x].get_text()
            elif x == 14:
                killgame = soup.select(".value")[x].get_text()
            elif x == 15:
                killmin = soup.select(".value")[x].get_text()
        playtime = soup.find('span', {'class': 'playtime'}).get_text()
        playtime = playtime[11:-19]
        matches = soup.find('span', {'class': 'matches'}).get_text()
        matches = matches[11:-17]

        embed = discord.Embed(title=playerNickname + "님의 전적 (PS4)", description="made by 빨강고양이", color=HyperScape_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이타임", value=playtime, inline=True)
        embed.add_field(name="게임 수", value=matches + '게임', inline=True)
        embed.add_field(name="K/d", value=kda, inline=True)
        embed.add_field(name="승리", value=wins + '게임', inline=True)
        embed.add_field(name="승리 비율", value=winper, inline=True)
        embed.add_field(name="평균 생존 시간", value=avgservivaltime, inline=True)
        embed.add_field(name="왕관 획득", value=crownper + '%', inline=True)
        embed.add_field(name="왕관으로 이긴 게임", value=crownwins + '게임', inline=True)
        embed.add_field(name="킬", value=kills + '킬', inline=True)
        embed.add_field(name="어시스트", value=assists, inline=True)
        embed.add_field(name="파괴한 보급품", value=chests + '개', inline=True)
        embed.add_field(name="합성된 아이템 수", value=fusions + '개', inline=True)
        embed.add_field(name="부활", value=revives + '회', inline=True)
        embed.add_field(name="왕관 획득 수", value=crownpickup + '번', inline=True)
        embed.add_field(name="총합 데미지", value=damagedone, inline=True)
        embed.add_field(name="헤드샷 비율", value=headshotper, inline=True)
        embed.add_field(name="게임당 킬수", value=killgame + '킬', inline=True)
        embed.add_field(name="분당 킬수", value=killmin + '킬', inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")
    await ctx.send(embed=embed)
    print(playerNickname)

@app.command()
async def xbox(ctx, *, playerNickname):
    webpage = requests.get('https://tracker.gg/hyper-scape/profile/xbl/' + playerNickname + '/overview')
    html = webpage.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        error = soup.find('h1').get_text()
    except AttributeError as e:
        error = 'none'

    # if (playerNickname == 'Red_cat2020'):
    #     embed = discord.Embed(title="개발자의 전적은 비밀입니다 ㅎㅎ", description="made by 빨강고양이", color=Error_Color)
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
    #     embed.add_field(name="플레이어 정보를 찾지 못함", value="닉네임 오류!", inline=True)
    #     embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")

    if (error == '404'):
        embed = discord.Embed(title="error", description="made by 빨강고양이", color=Error_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이어 정보를 찾지 못함", value="명령어, 닉네임이 정확한지 다시 한번 확인해주세요", inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")

    else:
        for x in range(0, 16):
            if x == 0:
                kda = soup.select(".value")[x].get_text()
            elif x == 1:
                wins = soup.select(".value")[x].get_text()
            elif x == 2:
                winper = soup.select(".value")[x].get_text()
            elif x == 3:
                avgservivaltime = soup.select(".value")[x].get_text()
            elif x == 4:
                crownper = soup.select(".value")[x].get_text()
            elif x == 5:
                crownwins = soup.select(".value")[x].get_text()
            elif x == 6:
                kills = soup.select(".value")[x].get_text()
            elif x == 7:
                assists = soup.select(".value")[x].get_text()
            elif x == 8:
                chests = soup.select(".value")[x].get_text()
            elif x == 9:
                fusions = soup.select(".value")[x].get_text()
            elif x == 10:
                revives = soup.select(".value")[x].get_text()
            elif x == 11:
                crownpickup = soup.select(".value")[x].get_text()
            elif x == 12:
                damagedone = soup.select(".value")[x].get_text()
            elif x == 13:
                headshotper = soup.select(".value")[x].get_text()
            elif x == 14:
                killgame = soup.select(".value")[x].get_text()
            elif x == 15:
                killmin = soup.select(".value")[x].get_text()
        playtime = soup.find('span', {'class': 'playtime'}).get_text()
        playtime = playtime[11:-19]
        matches = soup.find('span', {'class': 'matches'}).get_text()
        matches = matches[11:-17]

        embed = discord.Embed(title=playerNickname + "님의 전적 (XBOX)", description="made by 빨강고양이", color=HyperScape_Color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/708693776180314223/743432880969220156/Untitled-1.png")
        embed.add_field(name="플레이타임", value=playtime, inline=True)
        embed.add_field(name="게임 수", value=matches + '게임', inline=True)
        embed.add_field(name="K/d", value=kda, inline=True)
        embed.add_field(name="승리", value=wins + '게임', inline=True)
        embed.add_field(name="승리 비율", value=winper, inline=True)
        embed.add_field(name="평균 생존 시간", value=avgservivaltime, inline=True)
        embed.add_field(name="왕관 획득", value=crownper + '%', inline=True)
        embed.add_field(name="왕관으로 이긴 게임", value=crownwins + '게임', inline=True)
        embed.add_field(name="킬", value=kills + '킬', inline=True)
        embed.add_field(name="어시스트", value=assists, inline=True)
        embed.add_field(name="파괴한 보급품", value=chests + '개', inline=True)
        embed.add_field(name="합성된 아이템 수", value=fusions + '개', inline=True)
        embed.add_field(name="부활", value=revives + '회', inline=True)
        embed.add_field(name="왕관 획득 수", value=crownpickup + '번', inline=True)
        embed.add_field(name="총합 데미지", value=damagedone, inline=True)
        embed.add_field(name="헤드샷 비율", value=headshotper, inline=True)
        embed.add_field(name="게임당 킬수", value=killgame + '킬', inline=True)
        embed.add_field(name="분당 킬수", value=killmin + '킬', inline=True)
        embed.set_footer(text="serviced by hyper scape korea", icon_url="https://media.discordapp.net/attachments/708693776180314223/731835374619328619/HS.png?width=684&height=684")
    await ctx.send(embed=embed)
    print(playerNickname)

app.run(token)