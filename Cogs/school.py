from discord.ext import commands
from utils.config.main import Time
from utils.schoolMeal.school_meal import school_information, GetMealToday, GetMealTomorrow
from utils.image.main import SchoolImage
from utils.database.main import Main

prefix = Main.prefix


class School(commands.Cog, name='급식'):
  f"""
  디스코드 봇(아서)의 급식 명령어가 있는 카테고리입니다.
  명령어에 대한 정보를 상세히 알고 싶다면
  {prefix}도움말 [명령어]
  """
  school_meal = ['급식', '내일 급식', '내일급식']

  def __init__(self, app):
    self.app = app

  @commands.command(name='대소고', help='대소고 하루 급식을 보여준다.', usage=f'{prefix}대소고 [급식 or 내일 급식 or 내일급식]')
  async def dgsw_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('D10', '7240454', Time.get_time_today()), SchoolImage.DGSWLogo, '대소고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('D10', '7240454', Time.get_time_tomorrow()), SchoolImage.DGSWLogo, '대소고').embed)

  @commands.command(name='문화고', help='문화고 하루 급식을 보여준다', usage=f'{prefix}문화고 [급식 or 내일 급식 or 내일급식]')
  async def moonhwa_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750172', Time.get_time_today()), SchoolImage.MoonhwaLogo, '문화고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750172', Time.get_time_tomorrow()), SchoolImage.MoonhwaLogo, '문화고').embed)

  @commands.command(name='예일고', help='예일고 하루 급식을 보여준다', usage=f'{prefix}예일고 [급식 or 내일 급식 or 내일급식]')
  async def yale_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750772', Time.get_time_today()), SchoolImage.YaleLogo, '예일고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750772',Time. get_time_tomorrow()), SchoolImage.YaleLogo, '예일고').embed)

  @commands.command(name='계림고', help='계림고 하루 급식을 보여준다', usage=f'{prefix}계림고 [급식 or 내일 급식 or 내일급식]')
  async def gyerim_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750083', Time.get_time_today()), SchoolImage.GyerimLogo, '계림고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750083', Time.get_time_tomorrow()), SchoolImage.GyerimLogo, '계림고').embed)

  @commands.command(name='동성고', help='동성고 하루 급식을 보여준다', usage=f'{prefix}동성고 [급식 or 내일 급식 or 내일급식]')
  async def dongsug_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750542', Time.get_time_today()), SchoolImage.DongsugLogo, '동성고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750542', Time.get_time_tomorrow()), SchoolImage.DongsugLogo, '동성고').embed)

  @commands.command(name='신라공고', help='신라공고 하루 급식을 보여준다', usage=f'{prefix}신라공고 [급식 or 내일 급식 or 내일급식]')
  async def silla_tachnical_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750323', Time.get_time_today()), SchoolImage.SillaTachnicalLogo, '신라공고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750323', Time.get_time_tomorrow()), SchoolImage.SillaTachnicalLogo, '신라공고').embed)

  @commands.command(name='포철공고', help='포철공고 하루 급식을 보여준다', usage=f'{prefix}포철공고 [급식 or 내일 급식 or 내일급식]')
  async def pohang_jecheol_tachnical_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750337', Time.get_time_today()), SchoolImage.PohangJecheolTachnicalLogo, '포철공고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750337', Time.get_time_tomorrow()), SchoolImage.PohangJecheolTachnicalLogo, '포철공고').embed)

  @commands.command(name='경북외고', help='경북외고 하루 급식을 보여준다', usage=f'{prefix}경북외고 [급식 or 내일 급식 or 내일급식]')
  async def gyeongbuk_foreign_language_meal(self, ctx, *, meal):
    if meal in self.school_meal[0]:
      await ctx.send(embed=GetMealToday(school_information('R10', '8750079', Time.get_time_today()), SchoolImage.ForeignLanguageLogo, '경북외고').embed)
    elif meal in self.school_meal and meal is not self.school_meal[0]:
      await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750079', Time.get_time_tomorrow()), SchoolImage.ForeignLanguageLogo, '경북외고').embed)

  @commands.command(name='문급', help='문화고 하루 급식을 보여준다', uasge=f'{prefix}문급')
  async def short_moonhwa_today_meal(self, ctx):
    await ctx.send(embed=GetMealToday(school_information('R10', '8750172', Time.get_time_today()), SchoolImage.MoonhwaLogo, '문화고').embed)

  @commands.command(name='문내급', help='문화고 하루 급식을 보여준다', usage=f'{prefix}문내급')
  async def short_moonhwa_tomorrow_meal(self, ctx):
    await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750172', Time.get_time_tomorrow()), SchoolImage.MoonhwaLogo, '문화고').embed)

  @commands.command(name='예급', help='예일고 하루 급식을 보여준다', usage=f'{prefix}예급')
  async def short_yale_today_meal(self, ctx):
    await ctx.send(embed=GetMealToday(school_information('R10', '8750772', Time.get_time_today()), SchoolImage.YaleLogo, '예일고').embed)

  @commands.command(name='예내급', help='예일고 하루 급식을 보여준다', usage=f'{prefix}예내급')
  async def short_yale_tomorrow_meal(self, ctx):
    await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750772', Time.get_time_tomorrow()), SchoolImage.YaleLogo, '예일고').embed)

  @commands.command(name='예급내', help='예일고 하루 급식을 보여준다', usage=f'{prefix}예급내')
  async def short_yale_tomorrow_meal(self, ctx):
    await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750772', Time.get_time_tomorrow()), SchoolImage.YaleLogo, '예일고').embed)

  @commands.command(name='동급', help='동성고 하루 급식을 보여준다', usage=f'{prefix}동급')
  async def short_dongsug_today_meal(self, ctx):
    await ctx.send(embed=GetMealToday(school_information('R10', '8750542', Time.get_time_today()), SchoolImage.DongsugLogo, '동성고').embed)

  @commands.command(name='동내급', help='동성고 하루 급식을 보여준다', usage=f'{prefix}동내급')
  async def short_dongsug_tomorrow_meal(self, ctx):
    await ctx.send(embed=GetMealTomorrow(school_information('R10', '8750542', Time.get_time_tomorrow()), SchoolImage.DongsugLogo, '동성고').embed)


def setup(app):
  app.add_cog(School(app))
