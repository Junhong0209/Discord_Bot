########## 외부 라이브러리 ##########
import discord
import asyncio

########## 같은 폴더 안에 있는 다른 파이썬 파일 ##########
import config
import utils
import database
import Bot_token
import get_time

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

########## token 가져오기 ##########
token = Bot_token.Bot_Token.token

########## embed color 가져오기 ##########
Color = config.Config.Color
Error_Color = config.Config.Error_Color
HyperScape_Color = config.Config.HyperScape_Color

########## school logo 가져오기 ##########
DGSW_Logo = database.DGSW_Logo
YALE_Logo = database.YALE_Logo
MONNHWA_Logo = database.MOONHWA_Logo
DONSUNG_Logo = database.DONGSUNG_Logo
SILLA_TACHNICAL_Logo = database.SILLA_TACHNICAL_Logo
POHANG_JECHEOL_TACHNICAL_Logo = database.POHANG_JECHEOL_TACHNICAL_Logo
DOOWON_TECHNICL_Logo = database.DOOWON_TECHNICAL_Logo

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
    embed = discord.Embed(title="명령어 모음", description="", colour=Color)
    embed.add_field(name="!안녕", value="봇이 인사를 함", inline=False)
    embed.add_field(name="!빡추 [이름]", value="들어간 이름이 빡추 스탯을 쌓음", inline=False)
    embed.add_field(name="!초대링크", value="봇 초대 링크를 보내줌", inline=False)
    embed.add_field(name="!핲스 도움말", value="하이퍼 스케이프 전적 검색에 사용되는 명령어를 알려준다.", inline=False)
    embed.add_field(name="!씹덕 [이름]", value="말 그대로 씹덕.....", inline=False)
    embed.add_field(name="!급식", value="급식과 관련된 도움말 알려줌", inline=False)
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
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
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
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
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750172', today), MONNHWA_Logo, '문화고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750172', tomorrow), MONNHWA_Logo, '문화고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 예일고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750772', today), YALE_Logo, '예일고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750772', tomorrow), YALE_Logo, '예일고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 신라공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750323', today), SILLA_TACHNICAL_Logo, '신라공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750323', tomorrow), SILLA_TACHNICAL_Logo, '신라공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 동성고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750542', today), DONSUNG_Logo, '동성고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750542', tomorrow), DONSUNG_Logo, '동성고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 포철공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('R10', '8750337', today), POHANG_JECHEOL_TACHNICAL_Logo, '포철공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('R10', '8750337', tomorrow), POHANG_JECHEOL_TACHNICAL_Logo, '포철공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

@bot.command()
async def 두원공고(ctx, *, schoolMeal):
    today = get_time.get_time_today()
    tomorrow = get_time.get_time_tomorrow()

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('J10', '7531257', today), DOOWON_TECHNICL_Logo, '두원공고')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('J10', '7531257', tomorrow), DOOWON_TECHNICL_Logo, '두원공고')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())

#################### 명령어 ####################

@bot.command()
async def 제작자(ctx): # 자신의 정보를 넣으면 된다.
    embed = discord.Embed(title="제작자 정보", color=Color)
    embed.add_field(name="Discord", value="빨강고양이#5278", inline=False)
    embed.add_field(name="GitHub", value="[제작자의 GitHub](https://github.com/Junhong0209)", inline=False)
    embed.add_field(name="Facebook", value="[제작자의 Facebook](https://www.facebook.com/Junhong04/)", inline=False)
    embed.add_field(name="Instargram", value="[제작자의 Instargram](https://www.instagram.com/junhong936/)", inline=False)
    embed.add_field(name="Blog", value="[제작자의 Blog](https://junhong0209.github.io)", inline=False)
    embed.set_footer(text='made by 빨강고양이', icon_url='https://cdn.discordapp.com/attachments/819001182369611807/819001250850668605/9965e852f4552224.png')
    await ctx.send(embed=embed)

@bot.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def Hello(ctx):
    await ctx.send('안녕하세요~! {0.author.mention}님. 오늘도 좋은 하루 보내세요!'.format(ctx))

@bot.command()
async def 초대링크(ctx):
    embed = discord.Embed(title="봇 초대 링크", description="", color=Color)
    embed.add_field(name="이 봇을 다른 서버에 초대하기 위한 링크입니다.",
                    value="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=793085952254803988&permissions=8&scope=bot)",
                    inline=False)
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

bot.run(token)