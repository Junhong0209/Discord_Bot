# 아서 봇



구글링을 하여 제가 만들고 싶은 기능 들을 만들어본 봇입니다.

## Self Hosting

#### Python Version

```Python 3.8.5```

[Python Download](https://www.python.org/downloads/)

#### 필요한 모듈

```
discord
asyncio
youtube_dl
requests
datetime
```

#### 필요한 모듈 다운로드 방법

Win키를 누르고 CMD를 입력한다.
그런후 CMD창에 아래의 명령어를 하나씩 친다.
```
pip install discord
pip install asyncio
pip install youtube_dl
pip install requests
pip install datetime
```

#### Bot Token

`config.py`파일을 텍스트 편집기로 여시면 4번째 줄에 아래와 같이 있습니다.

```python
token = 'your bot token'
```

## 명령어

#### 도움말 명령어
```
!명령어 - 아서 봇이 가지고 있는 모든 명령어를 보여준다.
!급식 - 급식 조회와 관련된 모든 명령어를 보여준다.
// !핲스 명령어 - 하이퍼 스케이프와 관련된 모든 명령어를 보여준다. (현재 Code Repactoring 중....)
```

#### 명령어 모음
```
!제작자 - 이 봇을 만든 제작자의 정보를 보여준다.
!안녕 or !안녕하세요 or !ㅎㅇ - 봇이 인사를 한다.
!빡추 [이름] - 들어간 이름이 빡추 스탯을 쌓는다.
!초대링크 - 아서 봇을 초대할 수 있는 링크를 보여준다.
!관리자 - 현재 자기가 속해 있는 서버에서 관리자 권한을 가지고 있는지 확인하는 명령어다.
// !공지 - 서버의 관리자 권한을 가지고 있다면, 특정채널에 공지를 쓸 수 있는 명령어다. (현재 제작 중....)
```

#### 급식 명령어
```
![학교이름] 급식 - 해당 학교의 하루 급식을 보여줌
![학교이름] 내일급식 or ![학교이름] 내일 급식 - 해당 학교의 다음날 급식을 보여줌
# 현재 위 기능은 날짜를 매일 받아오는 코드로 만들지 못하였으므로 매일 봇을 다시 켜주어야 한다.
* 현재 등록 되어 있는 학교 - 대구 소프트웨어 마이스터 고등학교, 경주 문화 고등학교, 경주 예일 고등학교, 경주 신라 공업 고등학교, 포항 동성 고등학교, 포항 제철 공업 고등학교, 두원 공업 고등학교)
```

#### 하이퍼 스케이프 전적 검색 명령어
```
//!pc [닉네임] - PC용 하이퍼 스케이프 전적 검색
//!ps4 [닉네임] - PS4용 하이퍼 스케이프 전적 검색
//!xbox [닉네임] - XBOX용 하이퍼 스케이프 전적 검색
# 위 명령어들은 Code Repactoring으로 인하여 현재 구현되어있지 않음.
```

## 급식 명령어 중 새로운 학교 등록 방법
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
async def 학교명 입력(ctx, *, schoolMeal):
    if schoolMeal == SchoolMeal[0]:
        Embed = utils.getMeal_Today({
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': '시도교육청코드 입력',  
            'SD_SCHUL_CODE': '표준학교코드 입력',
            'MLSV_YMD': today  # 급식일자
        }
        , 학교 로고, '학교명 입력')
        await ctx.send(embed=Embed.embed)

    elif schoolMeal == SchoolMeal[1] or schoolMeal == SchoolMeal[2]:
        Embed = utils.getMeal_Tomorrow({
            'Type': 'json',
            'ATPT_OFCDC_SC_CODE': '시도교육청코드 입력',
            'SD_SCHUL_CODE': '표준학교코드 입력',
            'MLSV_YMD': tomorrow  # 급식일자
        }
        , 학교 로고, '학교명 입력')
        await ctx.send(embed=Embed.embed)

    else:
        await ctx.send(embed=utils.Error())
```
위 코드에서 학교 로고는 ``database.py`` 파일에 새로 학교 이름으로 변수(영어로 자기가 알아 볼 수 있도록)를 만든 후 뒤에 링크를 넣어준다.
그런 다음, ``main.py`` 파일로 돌아와 ``school logo 가져오기``에 새롭게 변수를 적고 등록한다. (방법은 아래 예시처럼)
```python
DGSW_Logo = database.DGSW_Logo
```
