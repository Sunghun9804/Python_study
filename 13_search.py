# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2 라는 값은 어디에 있는가?
print(f'2는 어디?:{a.index(2)}')
print(f'G는 어디?:{a.index('G')}') # G 는 2개 이지만 처음 찾는 값만 알려준다.

# 5번 인덱스 부터 'G'를 찾아라
print(f'G는 어디?:{a.index('G',5)}')
# 값이 없으면 에러(예외)를 발생 시킨다.
# print(a.index('H'))

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아보세요.

# 일일이 찾아보자
# idx = b.index(3,0)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1)
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5)
# print(f'3의 값은 {idx}번에 있다.')

# 다른방법1 while 함수를 활용해보자
# idx = 0
# while True:
#     idx = b.index(3, idx)
#     print(f'3의 값은 {idx}번에 있다.')
#     idx += 1

# 다른방법2 for 함수와 if 함수를 활용해보자
idx = 0
for n in b:
    # print(f'{idx}:{n}')
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    idx += 1

# 리스트 요소 삭제
# del a[3] 과 a.remove(3)
# del 은 특정 인덱스의 값을 지운다.
# remove 는 해당 값을 지운다.

print(f'a:{a}')
a.remove(3)
print(f'a:{a}')

# pop() = append() 의 개념
# 맨마지막 요소를 빼낸다.(리스트에서 사라진다.)
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

# count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
print(a)
print(f'a 안에 3인 값은 {a.count(3)}개가 있다.')
print(f'a 안에 9인 값은 {a.count(9)}개가 있다.') # 없는 값은 0을 반환

# a 안에 있는 모든 3을 지워주세요

# 1번 방법
# for n in a:
#     if n == 3:
#         a.remove(3)
#     print(a)

# 2번 방법
while True:
    a.remove(3)
    if a.count(3) == 0:
        break
print(a)









































