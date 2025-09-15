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

# 사전에 특정 요소를 꺼내보자(사용법은 List 와 비슷하다.)
# key를 직접 입력
print(dic2['name'])
print(dic2['friends'])

# get()함수 사용
print(dic2.get('phone'))
# 특정 키가 없는경우 None이 아닌 대체 내용으로 반환할수 있음
print(dic2.get('nick')) # -> 실행하면 None 나옴
print(dic2.get('nick','해당 내용이 없음')) # -> "해당 내용이 없음" 으로 나옴