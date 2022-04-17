# 아서 봇

구글링을 하여 제가 만들고 싶은 기능들을 만들어본 봇입니다.

## 명령어

***

### 카테고리: **``기본``**
```
;도움말 - 아서 봇이 가지고 있는 명령어를 카테로기 별로 분류해서 보여준다.
;빡추 [이름] - 뒤에 들어간 이름이 빡추 스텟을 쌓는다.
;제작자 - 제작자의 정보를 보여준다.
```

상세 도움말
```diff
! 아래 명령어는 도움말 명령어를 다른 방식으로 사용쓸 수 있는 방법입니다.

;도움말 [카테고리 명] - 해당 카테고리에 있는 명령어를 보여준다.
;도움말 [명령어 명] - 해당 명령어의 사용법 및 설명를 보여준다.
```

### 카테고리: **``게임``**
```diff
————— League of Legend
;롤랭크 [소환사 이름] - 해당 소환사의 롤 랭크 점수를 보여준다.
;롤전적 [소환사 이름] - 해당 소환사의 최근 5판 전적을 보여준다.
! 위 명령어는 OP.GG 사이트를 크롤링하여 만든 명령어입니다.

————— Overwatch
;OWP [배틀태그] - 해당 배틀태그 계정의 프로필을 보여준다.
;OWS [배틀태그] - 해당 배틀태그 계정의 전적을 보여준다.
! 위 명령어는 블리자드에서는 공식 API를 지원하지 않아 서드파티 API를 이용하여 만든 명령어입니다.

————— HyperScape
;pc [플레이어 명] - pc용 하이퍼 스케이프 전적을 보여준다.
;ps4 [플레이어 명] - ps4용 하이퍼 스케이프 전적을 보여준다.
;xbox [플레이어 명] - xbox용 하이퍼 스케이프 전적을 보여준다.
! 위 명령어는 tracker.gg 사이트를 크롤링하여 만든 명령어입니다.
```

### 카테고리 **``급식``**
```diff
;경북외고 [급식 or 내일 급식] - 경북외고 하루 급식을 보여준다.
;계림고 [급식 or 내일 급식] - 계림고 하루 급식을 보여준다.
;대소고 [급식 or 내일 급식] - 대소고 하루 급식을 보여준다.
;동성고 [급식 or 내일 급식] - 동성고 하루 급식을 보여준다.
;문화고 [급식 or 내일 급식] - 문화고 하루 급식을 보여준다.
;신라공고 [급식 or 내일 급식] - 신라공고 하루 급식을 보여준다.
;예일고 [급식 or 내일 급식] - 예일고 하루 급식을 보여준다.
;포철공고 [급식 or 내일 급식] - 포철공고 하루 급식을 보여준다.

! 아래 명령어는 짧게 사용가능한 단축 명령어입니다.
! 단축 명령어를 등록하고 싶다면 빨강고양이#5278로 어떻게 단축하고 싶은지 알려주세요.
;동급 or ;동내급 - 동성고 하루 급식을 보여준다.
;문급 or ;문내급 - 문화고 하루 급식을 보여준다.
;예급 or ;예내급 - 예일고 하루 급식을 보여준다.

! 학교 추가를 원하면 빨강고양이#5278로 지역과 학교이름을 알려주세요.
```

### 카테고리 **``관리자``**
```diff
- 이 명령어들은 서버의 관리자가 아니면 사용할 수 없습니다.
;채널설정 [#채널 명] - 공지를 보낼 채널을 설정한다.
;공지작성 [할 말] - 설정한 채널에 공지를 작성한다.

! 아래 명령어는 관리자가 아니여도 사용이 가능합니다.
;권한 - 해당 서버에서 유저가 관리자 권한이 있는지 확인한다.
```