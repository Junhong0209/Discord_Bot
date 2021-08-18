# 급식 명령어 사용할 학교 신규 등록 방법

[나이스 교육정보 개방 포털](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=1)에 접속하여 아래 설명대로 하면 된다.

```
1. 시도교육청을 선택한다. (자신의 학교가 속해있는 시도교육청을 선택해야한다.)
2. 학교명을 입력한다.
3. 급식 일자를 오늘 하루로 설정한다.
4. 검색 버튼을 누르면 아래에 학교의 급식이 뜬다.
5. 그 곳에서 자신의 학교의 시도교육청코드와 표준학교코드를 복사 해놓는다.
```
시도교육청코드와 표준학교코드를 복사 했다면 아래의 코드처럼 추가하자.
```python
@app.command()
async def 학교명(ctx, *, schoolMeal):
    today = get_time.get_time_today()          # 명령어를 사용하면 함수를 이용하여 현재 날짜을 가져옴
    tomorrow = get_time.get_time_tomorrow()    # 명령어를 사용하면 함수를 이용하여 내일 날짜을 가져옴

    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today(utils.school_information('시도교육청코드', '표준학교코드', today), 학교 로고 변수 명, '학교 이름')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow(utils.school_information('시도교육청코드', '표준학교코드', tomorrow), 학교 로고 변수 명, '학교 이름')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())
```
위 코드에서 학교 로고는 ``database.py`` 파일에 새로 학교 이름으로 변수(영어로 자기가 알아 볼 수 있도록)를 만든 후 뒤에 링크를 넣어준다.
그런 다음, ``main.py`` 파일로 돌아와 ``school logo 가져오기``에 새롭게 변수를 적고 등록한다. (방법은 아래 예시처럼)

```python
DGSW_Logo = database.DGSW_Logo
```