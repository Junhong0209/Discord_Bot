########## 외부 라이브러리 ##########
import discord
import asyncio
from discord.ext import commands

########## 같은 폴더 안에 있는 다른 파이썬 파일 ##########
import config
import utils
import database
import Bot_token
import get_time

import GameRecordSearch.HyperScapeRecordSearch


bot = commands.Bot(command_prefix='!')

########## token 가져오기 ##########
token = Bot_token.Bot_Token.token

########## embed color 가져오기 ##########
Color = config.Config.Color
Error_Color = config.Config.Error_Color
HyperScape_Color = config.Config.HyperScape_Color

########## school logo 가져오기 ##########
DGSW_Logo = database.DGSW_Logo
Yale_Logo = database.Yale_Logo
Moonhwa_Logo = database.Moonhwa_Logo
Dongsug_Logo = database.Dongsug_Logo
Silla_Tachnical_Logo = database.Silla_Tachnical_Logo
Pohang_Jecheol_Tachnical_Logo = database.Pohang_Jecheol_Tachnical_Logo
Doowon_Tachnical_Logo = database.Doowon_Tachnical_Logo
Gyerim_Logo = database.Gyerim_Logo

########## img 가져오기 ##########
developerImg = database.icon

@bot.event
async def on_ready():
    print('Loggend-in Bot:', bot.user.name)
    print('Bot id:', bot.user.id)
    print('connection was succesful')
    print('=' * 30)

    game = discord.Game('정신 차리기')
    await bot.change_presence(status=discord.Status.offline, activity=game)
    await asyncio.sleep(5)
    while True:
        game = discord.Game('빡추 스탯 쌓기')
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('여전히 베타 테스트 중이에요~')
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('테스트가 언제 쯤 끝날까요~')
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game('!도움말')
        await bot.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)

#################### 도움말 ####################

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title="명령어 모음", colour=Color)
    embed.add_field(name="!안녕", value="봇이 인사를 한다.", inline=False)
    embed.add_field(name="!빡추 [이름]", value="들어간 이름이 빡추 스탯을 쌓는다.", inline=False)
    embed.add_field(name="!초대링크", value="봇 초대 링크를 보내준다.", inline=False)
    # embed.add_field(name="!핲스 도움말", value="하이퍼 스케이프 전적 검색에 사용되는 명령어를 알려준다.", inline=False)
    embed.add_field(name="!급식", value="급식과 관련된 도움말 알려준다.", inline=False)
    embed.add_field(name="!공지작성 [공지로 할 말]", value="서버의 관리자 권한을 가지고 있다면, 특정 채널에 공지를 쓸 수 있는 명령어다.")
    embed.add_field(name="!관리자", value="현재 서버에서 이 명령어를 사용한 사람이 관리자 권한을 가지고 있는지 알려준다.")
    embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)
    await ctx.send(embed=embed)

@bot.command()
async def 급식(ctx):
    embed = discord.Embed(title='급식 도움말', color=Color)
    embed.add_field(name="!대소고 급식", value="대소고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="!문화고 급식", value="문화고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="!예일고 급식", value="예일고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="!신라공고 급식", value="신라공고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="!동성고 급식", value="동성고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="!포철공고 급식", value="포철공고 하루 급식을 보여준다.", inline=False)
    embed.add_field(name="![학교 이름] 급식", value="추후 다른 고등학교 추가 예정", inline=False)
    embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)
    await ctx.send(embed=embed)

#################### 급식 조회 ####################

SchoolMeal = ['급식', '내일 급식', '내일급식']

@bot.command()
async def 대소고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('D10', '7240454', today), DGSW_Logo, '대소고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('D10', '7240454', tomorrow), DGSW_Logo, '대소고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 문화고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750172', today), Moonhwa_Logo, '문화고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750172', tomorrow), Moonhwa_Logo, '문화고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 예일고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750772', today), Yale_Logo, '예일고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750772', tomorrow), Yale_Logo, '예일고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 신라공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750323', today), Silla_Tachnical_Logo, '신라공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750323', tomorrow), Silla_Tachnical_Logo, '신라공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 동성고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750542', today), Dongsug_Logo, '동성고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750542', tomorrow), Dongsug_Logo, '동성고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 포철공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750337', today), Pohang_Jecheol_Tachnical_Logo, '포철공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750337', tomorrow), Pohang_Jecheol_Tachnical_Logo, '포철공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 두원공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('J10', '7531257', today), Doowon_Tachnical_Logo, '두원공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('J10', '7531257', tomorrow), Doowon_Tachnical_Logo, '두원공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 계림고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750083', today), Gyerim_Logo, '계림고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == [2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750083', tomorrow), Gyerim_Logo, '계림고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

#################### 핲스 전적 검색 명령어 ####################

@bot.command()
async def PC(ctx, *, playerNickname):
    Embed = GameRecordSearch.HyperScapeRecordSearch.HyperScapeRecordSearchPC(playerNickname)

    await ctx.send(embed=Embed.embed)

@bot.command()
async def PS4(ctx, *, playerNickname):
    Embed = GameRecordSearch.HyperScapeRecordSearch.HyperScapeRecordSearchPS4(playerNickname)

    await ctx.send(embed=Embed.embed)

@bot.command()
async def XBOX(ctx, *, playerNickname):
    Embed = GameRecordSearch.HyperScapeRecordSearch.HyperScapeRecordSearchXBOX(playerNickname)

    await ctx.send(embed=Embed.embed)

#################### 명령어 ####################

@bot.command()
async def 제작자(ctx):        # 자신의 정보를 넣으면 된다.
    embed = discord.Embed(title="제작자 정보", color=Color)
    embed.add_field(name="Discord", value="빨강고양이#5278", inline=False)
    embed.add_field(name="GitHub", value="[제작자의 GitHub](https://github.com/Junhong0209)", inline=False)
    embed.add_field(name="Facebook", value="[제작자의 Facebook](https://www.facebook.com/Junhong04/)", inline=False)
    embed.add_field(name="Instargram", value="[제작자의 Instargram](https://www.instagram.com/junhong936/)", inline=False)
    embed.add_field(name="Blog", value="[제작자의 Blog](https://dev-redcat.tistory.com/)", inline=False)
    embed.set_footer(text='Bot made by. 빨강고양이#5278', icon_url=developerImg)
    await ctx.send(embed=embed)

@bot.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def Hello(ctx):
    await ctx.send('안녕하세요~! {}님. 오늘도 좋은 하루 보내세요!'.format(ctx.author.mention))

@bot.command()
async def 초대링크(ctx):
    embed = discord.Embed(title="봇 초대 링크", color=Color)
    embed.add_field(name="이 봇을 다른 서버에 초대하기 위한 링크입니다.", value="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=793085952254803988&permissions=8&scope=bot)", inline=False)
    embed.set_footer(text="Bot made by. 빨강고양이#5278", icon_url=developerImg)
    await ctx.send(embed=embed)

@bot.command()
async def 빡추(ctx, *, text=None):
    if None == text:       # !빡추 명령어 뒤에 아무것도 입력 하지 않은 경우
        await ctx.send("누구를 입력하신거죠? 전 입력 받은게 없습니다만?")
    elif text == "아서":    # !빡추 명령어 뒤에 봇의 이름을 넣은 경우
        await ctx.send("나 빡추 아닌데?")
    else:
        await ctx.send("보셨나요? 보셨나요? 보셨냐구요!!!! " + text + "의 빡추 스탯쌓기!!")
        print(text)

@bot.command(name='관리자')
async def is_mange_messages(ctx):
    if ctx.guild:
        if ctx.message.author.guild_permissions.administrator:
            await ctx.send('이 서버의 관리자입니다.')
        else:
            await ctx.send('이 서버의 관리자가 아닙니다.')
    else:
        await ctx.send('DM으론 불가능합니다.')

@bot.command(name='공지작성')
async def Announcement(ctx, *, notice):
    i = ctx.message.author.guild_permissions.administrator
    channel = ctx.guild.get_channel(844527701300609044)  # 메시지를 보낼 채널 설정
    # Discord 에서 개발자 모드를 켜서 채널의 ID를 가져와 넣는다.
    
    if i is True:
        embed = discord.Embed(title="**Hotplace 공지사항**", description="공지사항은 항상 잘 숙지 해주시기 바랍니다.\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice), color=Color)
        embed.set_footer(text="Bot made by. 빨강고양이#5278 | 담당 관리자: {}".format(ctx.author), icon_url=developerImg)
        await channel.send("@everyone", embed=embed)
        await ctx.send("```**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(channel, ctx.author, notice))

    if i is False:
        await message.channel.send("{}, 당신은 관리자가 아닙니다".format(ctx.author.mention))

bot.run(token)