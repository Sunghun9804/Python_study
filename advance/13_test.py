import traceback

# text = input('값을 넣으면 숫자로 변환 됩니다.')
# num = int(text)
# print(f'당신이 입력한 값: {num} 이 숫자로 변환 되었습니다.')

# 값을 넣으면 숫자로 변환 시켜주는 코드를 작성했다.
# 우려되는 점은 꼭 숫자를 않넣는 사람들이 있을수도 있다는 점이다.
# 그런경우 에러가 발생할 것이다. -> ValueError: invalid literal for int() with base 10: '오'
# 값이 숫자가 입력되면 정상출력하고, 숫자가 아닌 나머지는 '올바른 값이 아닙니다.' 라는 안내문구를 작성해서 코드를 완성시켜보자.


# try('====끝====')


while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text} 는 숫자가 아닙니다.');