cup = 0 # cup이라는 변수에 0을 대입
running = True

while True: # while 은 오른쪽에 있는 조건 결과가 True 일 경우 반복되는 구문
    cup += 1 # 컵에다가 1씩 증가
    print(cup)
    if cup == 10: # cup 값이 10이라면? 아래 내용 출력
        # running = False
        break

print('while 문 종료')