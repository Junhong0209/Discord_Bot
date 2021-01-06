import discord
import openpyxl
import asyncio

client = discord.Client()

@client.event
async def on_ready():

    # console 창에 봇의 아이디, 닉네임이 출력되는 코드
    print("Logged-in Bot:", client.user.name)
    print("Bot id:", client.user.id)
    print("===========")

    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작 하는 중....")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("빡추 소환")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("아직 베타 테스트 중이예요~")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("/명령어")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)


@client.event
async def on_message(message):

    # 도움말
    if message.content == "/명령어":
        embed = discord.Embed(title="명령어", description="", color=0x62c1cc)  # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.add_field(name="!빡추 (이름)", value="봇이 아주 재밌는 말을 해줌", inline=False)
        embed.add_field(name="/제작자", value="제작자에 대해 알려줌", inline=False)
        embed.set_footer(text="제작자: 빨강고양이")  # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed)  # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

    if message.content == "/제작자":
        embed = discord.Embed(title="제작자 정보", color=0xFD02D2)
        embed.add_field(name="Discord", value="빨강고양이#5278", inline=False)
        embed.add_field(name="GitHub", value="[제작자의 GitHub](https://github.com/Junhong0209)", inline=False)
        embed.add_field(name="Facebook", value="[제작자의 Facebook](https://www.facebook.com/Junhong04/)", inline=False)
        embed.add_field(name="Instargram", value="[제작자의 Instargram](https://www.instagram.com/junhong936/)", inline=False)
        embed.add_field(name="Blog", value="[제작자의 Blog](https://junhong0209.github.io)", inline=False)
        await message.channel.send(embed=embed)

    # 어떠한 메세지를 입력하면 출력해주는 명령어
    if message.content.startswith("!빡추"):
        Name = message.content[3:len(message.content)]
        await message.channel.send("보셨나요? " + Name + "의 빡추 스탯 쌓기!")

    if message.content == "안녕하살법!":
        await message.channel.send("안녕하살법 받아치기!")

client.run("NzkzMDg1OTUyMjU0ODAzOTg4.X-nI2Q.CkLTYVLOLs1KUyg8uRpTxUUiScg")