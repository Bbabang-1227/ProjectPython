
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴

msg = '{}님 뭘 쳐다보세요'
print(msg.format('방현준')) # 순서 숫자 지정이 없다면 0부터
msg = '{1}님 뭘 쳐다보세요 {0}님 싸움잘하세요?'
print(msg.format('방현준응애', '방현준')) # 순서 숫자 지정이 없다면 0부터


# [참고] http://pyformat.info
# [나만참고] http://blog.naver.com/PostView.nhn?blogId=ksg97031&logNo=221126216595&parentCategoryNo=&categoryNo=172&viewDate=&isShowPopularPosts=true&from=search

# print format - printf() 역할
name = '홍길동'
age = 22
height = 170.456

print('%s님은 %d세이고 신장은 %3.3f cm입니다' % (name, age, height))


#--------------------------------------------------
# 실수인 경우


