import random

number = random.randint(1,31) # 숫자를 랜덤으로 부여합니다.
#print(f'내 마음속 숫자: {number}') # 랜덤으로 부여한 숫자를 내 마음속 숫자"로 표현하기 위해 f-string 사용합니다.
runnung = True # 다음 코드문에 while True 문은 조건이 참이기 때문에 무한으로 돌아가는 무한 반복문이라고 합니다. 즉 조건이 참(True)이면 while 함수가 돌아가고 거짓(False)이면 조건이 참이 아니기 때문에 작동이 안합니다. 왜 그런지는 모르겠습니다. 1+1은 왜 2인가요 같은 느낌적인 느낌

while runnung: #반복문 while이 돌아가도록 합니다?
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입합니다.
    print(f'입력받은 숫자{guess}') # 입력받는 숫자 프린트해서 알려줍니다.
    if guess > number: # 만약 guess(내가 생각한 숫자)가 number(입력받은 숫자) 클 경우
        print('내가 생각한 숫자보다 큽니다.') # 조건에 부합하면 '내가 생각한 숫자보다 큽니다.' 라는 문구를 나타냅니다. runnung = True이므로 계속 질문에 답을 해야 합니다.
    elif guess < number: # 만약 전 if단계(guess > number)에 조건이 맞지 않는다면 elif(=elseif의미)로 넘어와서 elif(=elseif의미)조건에 맞는지 안맞는지 확인합니다. elif(=elseif의미)조건은 (guess < number) 입니다.
        print('내가 생각한 숫자보다 작아요.') # 조건(guess < number)에 부합하면 '내가 생각한 숫자보다 작아요.'라는 문구를 나타냅니다. runnung = True이므로 계속 질문에 답을 해야 합니다.
    else: # 위 조건들 크지도 않고 작지도 않으면 자동으로 같기 때문에 경우의 수는 마음속 숫자와 내가 생각한 숫자가 같은 조건만 남습니다. guess == number
        print('내 마음속 숫자가 맞습니다') # '내 마음속 숫자가 맞습니다' 라는 문구를 나타냅니다
        runnung = False # runnung = True이면 계속 실행됩니다. 게임은 숫자가 일치하면 멈추도록 설계할려고 합니다. False 값을 지정해서 while 함수가 작동하지 않도록 코딩합니다.
print('게임 끝') # 게임의 끝 안내문을 나타냅니다.

# while runnung:
#     # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
#     guess = int(input('1~31 중 내가 생각한 숫자는?'))
#     print(f'입력받은 숫자{guess}')
#     if guess > number:
#         print(f'{guess} 가 내 마음속 숫자보다 크기 때문에 다시 돌려보세요')
#     if guess < number:
#         print(f'{guess}가 내 마음속 숫자보다 작기 때문에 다시 돌려보세요')
#     if guess == number:
#         runnung = False
#         print(f'내 마음속 숫자가 맞습니다')
# print('게임 끝')




