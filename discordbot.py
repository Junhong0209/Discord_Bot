import discord
import asyncio
from discord.ext import commands

token = "your bot token"

app = commands.Bot(command_prefix='!')
client = discord.Client()

@app.event
async def on_ready():
    print('Loggend-in Bot: ', app.user.name)
    print('Bot id: ', app.user.id)
    print('connection was succesful')
    print('=' * 30)
    await app.change_presence(status=discord.Status.offline)
    game = discord.Game('정신 차리기')
    await app.change_presence(status=discord.Status.online, activity=game)
    await asyncio.sleep(2)
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

#################### 명령어 ####################

@app.command()
async def 도움말(ctx):
    embed = discord.Embed(title="명령어 모음", description="", colour=0xFD02D2)
    embed.add_field(name="!안녕", value="봇이 인사를 함", inline=False)
    embed.add_field(name="!빡추 [이름]", value="들어간 이름이 빡추 스탯을 쌓음", inline=False)
    embed.add_field(name="!초대링크", value="봇 초대 링크를 보내줌", inline=False)
    embed.add_field(name="!뎅구", value="음.... 입력하면 뭐라고 할까....? 궁금하면 직접 해봐 ㅎ", inline=False)
    embed.add_field(name="!씹덕 [이름]", value="말 그대로 씹덕.....", inline=False)
    embed.add_field(name="!에코 [아무말]", value="봇이 똑같이 말함", inline=False)
    embed.add_field(name="!제작자", value="제작자의 정보를 알려줌", inline=False)
    await ctx.send(embed=embed)

@app.command()
async def 제작자(ctx): # 자신의 정보를 넣으면 된다.
    embed = discord.Embed(title="제작자 정보", color=0xFD02D2)
    embed.add_field(name="Discord", value="자신의 디스코드 태그", inline=False)
    embed.add_field(name="GitHub", value="[제작자의 GitHub](자신의 깃 허브 링크)", inline=False)
    embed.add_field(name="Facebook", value="[제작자의 Facebook](자신의 페이스북 링크)", inline=False)
    embed.add_field(name="Instargram", value="[제작자의 Instargram](자신의 인스타그램 링크)", inline=False)
    embed.add_field(name="Blog", value="[제작자의 Blog](자신의 블로그 링크)", inline=False)
    await ctx.send(embed=embed)

@app.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def Hello(ctx):
    await ctx.send('안녕하세요~! {0.author.mention}님. 오늘도 좋은 하루 보내세요!'.format(ctx))

@app.command()
async def 초대링크(ctx):
    embed = discord.Embed(title="봇 초대 링크", description="", color=0xFD02D2)
    embed.add_field(name="이 봇을 다른 서버에 초대하기 위한 링크입니다.", value="[봇 초대하기](이 곳에 자신이 만든 봇의 초대 링크를 넣으면 된다.)", inline=False)
    await ctx.send(embed=embed)

@app.command()
async def 빡추(ctx, *, text=None):
    if (text == None): # !빡추 명령어 뒤에 아무것도 입력 하지 않은 경우
        await ctx.send("누구를 입력하신거죠? 전 입력 받은게 없습니다만?")
    else:
        await ctx.send("보셨나요? " + text + "의 빡추 스탯쌓기!!")
        print(text)

@app.command()
async def 씹덕(ctx, text=None):
    if (text == None): # !씹덕 명령어 뒤에 아무것도 입력 하지 않은 경우
        await ctx.send("누구를 입력하신거죠? 전 입력 받은게 없습니다만?")
    else:
        await ctx.send("아, " + text + " 그 씹덕 샛기?")
        print(text)

@app.command()
async def 에코(ctx, *, content: str): # 이 기능은 자신이 한 말을 봇이 똑같이 다시 말하는 명령어이다.
    await ctx.send(content)

@app.command()
async def 안녕하살법(ctx):
    await ctx.send("안녕하살법 받아치기~!")

app.run(token)
