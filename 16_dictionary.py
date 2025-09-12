# 사전은 key:value 형태로 되어있다.
# 비슷한 자료구조로는 자바스크립트에는 오브젝트, 자바의 맵이 있다.

# 만들자마자 넣는 방법
# 열고닫고 먼저 꼭 하자!
dic = {'name':'Jeong seong-hun',
        'phone':'010-1234-1234',
        'age':55
}

dic2 = {'name':'Messi',
        'phone':'010-2233-5454',
        'friends':['Alice','John','Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)
# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)