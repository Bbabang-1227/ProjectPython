
from datetime import date,datetime,timedelta

# 날짜
today = date.today();
print('today is ', today)

# 연, 월 ,일 출력
print(today.year)
print(today.month)
print(today.day)

# 현재의 날짜와 시간구하기
curtime = datetime.today()
print(curtime)

today = date.today()
print(today + timedelta(days= -1))
print(today + timedelta(days= -7))
print(today + timedelta(days= +10))

# 날짜 출력 형식(strftime)
today = date.today()
print(today.strftime('%m/%d/%y'))

# 문자열을 날짜 형식으로(strptime)
str = '2021-06-24 16:15:30'
mydate = datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
print(mydate)
