cup = 0 # cup이라는 변수에 0을 대입
running = True

# while True: # while 은 오른쪽에 있는 조건 결과가 True 일 경우 반복되는 구문
#     cup += 1 # 컵에다가 1씩 증가
#     print(cup)
#     if cup == 10: # cup 값이 10이라면? 아래 내용 출력
#         # running = False
#         break # 반복문 자체를 실행종료

print('while 문 종료')

for i in range(1,10):
    # 방법1
    # if i == 3: # i가 3이라면? 밑에 내용 출력
    #     continue # 무시하라는 의미, 위에 조건이 i == 3 이므로 3만 제외하고 반복문 실행
    # if i == 6: # i가 6이라면? 밑에 내용 출력
    #     continue # 무시하라는 의미, 위에 조건이 i == 6 이므로 6만 제외하고 반복문 실행
    # if i == 9: # i가 9이라면? 밑에 내용 출력
    #     continue # 무시하라는 의미, 위에 조건이 i == 9 이므로 9만 제외하고 반복문 실행

    # 방법2
    if i%3 == 0:
        continue
    # 방법3
    # if (i == 3) | (i == 6) | (i == 9): # i가 3, 6, 9 라면? 밑에 내용 출력
    #     continue # 무시하라는 의미, 위에 조건이 i == 3 이므로 3만 제외하고 반복문 실행

    print(i)

