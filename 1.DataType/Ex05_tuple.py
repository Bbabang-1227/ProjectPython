"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1, 2, 3)
print(t[0])

t2 = 1, 2, 3
print(t2[-1])
t4 = (1,)
print(t4)
print((type(t4)))
# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# del t[1]   # 에러 발생
print('------------------- 2 -----------------')


# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')

# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')

# (5) 튜플 요소 풀기
print('------------------- 5 -----------------')
to = (1,2,3)
n1, n2, n3 = to
print(n1 + n2 + n3)

# (6) 튜플과 리스트 변환
print('------------------- 5 -----------------')
my_list = ['a','b','c']
my_tuple = ('x', 'y', 'z')
print(tuple(my_list))
print(list(my_tuple))