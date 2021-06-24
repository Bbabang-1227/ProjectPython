"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
"""

# ----------------------------------
# 단을 입력받아 구구단을 구하기
import sys

'''
name = input('이름 입력->')
age = int(input('나이 입력->'))
print('your name is %s.' % name)
print('your age is {0}.'.format(age + 1))

dan = int(input('input dan -> '))
for i in range(1, 10):
    print('%d * %d = %d' % (dan, i, dan * i))
'''


# -----------------------------------------
# print() 함수

print('뭘봐 너 싸움 잘하냐?')
for i in range(5):
    print(i, end=' ') # 개행문자 대신 공백문자 사용
# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3
import sys
args = sys.argv[1:]
for i in args:
    print(i)
    print('서버에 연결합니다')