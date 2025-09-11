# 콜라, 생수, 오렌지주스, 식혜, 이온음료
item = '생수'

# if문이 여러개 있으면 한칸식 띄어서 표시(개인취향)
if item =='콜라':
    print(f'{item} 가 나왔습니다.')

if item =='생수':
    print(f'{item} 가 나왔습니다.')

if item =='오렌지주스':
    print(f'{item} 가 나왔습니다.')

if item =='식혜':
    print(f'{item} 가 나왔습니다.')

if item =='이온음료':
    print(f'{item} 가 나왔습니다.')

#else if문 만들기
item = '커피'

if item == '콜라':
    print(f'{item} 가 나왔습니다.')

elif item == '생수':
    print(f'{item} 가 나왔습니다.')

elif item == '오렌지주스':
    print(f'{item} 가 나왔습니다.')

elif item == '식혜':
    print(f'{item} 가 나왔습니다.')

elif item == '이온음료':
    print(f'{item} 가 나왔습니다.')

else:
    print(f'{item} 은(는) 보유하지 않은 음료 입니다.')

