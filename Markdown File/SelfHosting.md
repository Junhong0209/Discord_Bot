# Discord Bot Self Hosting

### Python Version

```Python 3.8.5```

[Python Download](https://www.python.org/downloads/)

### 필요한 모듈

```
discord
asyncio
time
datetime
requests
```

### 필요한 모듈 다운로드 방법

Win키를 누르고 CMD를 입력한다.
그런후 CMD창에 아래의 명령어를 하나씩 친다.
```
# main.py에 필요한 라이브러리
pip install discord
pip install asyncio

# get_time.py에 필요한 라이브러리
pip install time
pip install datetime

# utils.py에 필요한 라이브러리
pip install requests
```

### Bot Token

`Bot_token.py`이라는 파일을 하나 새로 만들어 안에 아래와 같이 디스코드 봇의 토큰을 넣어주세요.

```python
class Bot_Token:
    token = "Your bot token"
```