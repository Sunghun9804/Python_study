# Function

# 함수(Function)의 정의
# "변수"가 데이터를 담는 무언가라면 "함수(Function)"는 동작을 실행해 주는 무언가 이다.
# 함수(Function) 구조

def 토스트기(빵): # 반환타입 O, 매개변수 O
    return "구운빵"

def 번호표기계(): # 반환타입 O, 매개변수 X
    return "번호표"

def 저금통(동전): # 반환타입 X, 매개변수 O
    print(동전, " 저금")

def 호출벨(): # 반환타입 X, 매개변수 X
    print("호출")

# -------------------------------------------------------------------------------------

# 인자 값(argument)의 종류
# 함수에 들어오는 변수의 이름은 다양 -> 인자 값(argument), reference 변수, parameter, 매개변수

# def function_name( args=5 ):
# def function_name( *args ):
# def function_name( **args ):

# -------------------------------------------------------------------------------------

# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0):
    result = num + 5
    return result

print(plus(5)) #10
print(plus()) # plus() missing 1 required positional argument: 'num'

# 인자값의 종류를 튜플(수정이 불가능한 List 형태)로만 받겠다.
def tuple_args(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total

# 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))

# ** 는 매개변수를 사전형태로 받겠다.
def dic_args(**dic):
    # 1. dic 에서 값만 빼온다.
    values = dic.values()
    #print(values)
    # 2. 이 값들을 하나씩 더해 누적시킨다.
    total = 0
    for v in values:
        #print(v)
        total += v
    # 3. 누적시킨 값을 밖으로 return 한다.
    return total
# 위 함수를 실행하면 입력된 값들의 합산이 반환되도록 하세요
result = dic_args(kim=50, lee=100, park=70, na=90)
print(result)

# -------------------------------------------------------------------------------------

# Function 의 설명서인 document 를 제작 할 수 있다.
# 자신이 만든 함수의 사용법을 ''' 또는 """ 로 제작이 가능하다.
# 함수명 .__doc__를 이용하여 설명을 볼 수도 있다.

def print_max(x, y):
    '''
    입력된 x와 y 중 큰 값을 알려주는 함수입니다.
    :param x: 인자값1
    :param y: 인자값2
    '''

    print(f'{x}와 {y} 중에...')
    if x > y:
        print(f'{x} 가 더 큽니다.')
    else:
        print(f'{y} 가 더 큽니다.')


print_max(5, 10)

# 해당 함수에 대한 출력
print(f'함수설명: {print_max.__doc__}')

# 우리는 누군가가 사용하기 위해 만들어 공개한 함수를 API
# 이 API 에 대한 설명문서를 API 문서라고 부른다.

# -------------------------------------------------------------------------------------

# API(Application Programming Interface)
# "응용 프로그램에서 사용할 수 있도록", 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스

# Interface : "실제로 하면 복잡한 일"을 간단하게 할 수 있도록 만들어 놓은 "어떤 장치"

# -------------------------------------------------------------------------------------

# 요약(Summary)
# 1. 함수는 def 라는 키워드를 사용한다.
# 2. 함수는 함수명, 매개변수, 반환문 으로 구성된다.
# 3. API 와 Interface 를 알아두자

# -------------------------------------------------------------------------------------

# oper

# 변수
field1 = 10
field2 = 'String'

# 함수
def sum(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devision(a,b):
    return a/b

# -------------------------------------------------------------------------------------

# Moduel

# 정의
# Moduel 은 작성된 프로그램을 다른 파일이나 사용자가 쓸 수 있도록 만들어 놓은 것 이다.
# Moduel 안에는 함수나 변수 등을 정의 해 놓을 수 있다.

# -------------------------------------------------------------------------------------

# Moduel 사용

# import 문을 사용하여 모듈을 불러오자
# 사용 후 실행 해보면 __pycache__ 폴더가 생성 된다.

# from oper import *           -> 모듈의 모든 함수를 사용
# from oper import sum         -> 모듈에서 한개의 함수를 사용
# from oper import sum, minus  -> 모듈의 복수개 함수를 사용
# from oper as op              -> oper 모듈을 불러와 op 라는 이름으로 사용

# from 모듈 import 함수
# 사용할 함수를 미리 불러놓고 사용하는 방법
from oper import sum
print(f'sum() 함수 실행: {sum(5,10)}')

# PyCharm 에서 실행하면...(예시)

# D:\STUDY\python\.venv\Scripts\python.exe D:\STUDY\python\advance\01_moduel_use.py
# sum() 함수 실행: 15
# 종료 코드 0(으)로 완료된 프로세스


# import 모듈
# 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법
import oper as op
print(f'minus() 함수실행: {op.minus(10,5)}')

# PyCharm 에서 실행하면...(예시)

# D:\STUDY\python\.venv\Scripts\python.exe D:\STUDY\python\advance\01_moduel_use.py
# minus() 함수실행: 5
# 종료 코드 0(으)로 완료된 프로세스

# import 모듈
# 변수도 불러다 사용 할 수 있다.
import oper as op
print(f'field1: {op.field1} / field2: {op.field2}')

# PyCharm 에서 실행하면...(예시)

# D:\STUDY\python\.venv\Scripts\python.exe D:\STUDY\python\advance\01_moduel_use.py
# field1: 10 / field2: String
# 종료 코드 0(으)로 완료된 프로세스

# -------------------------------------------------------------------------------------

# moduel의 이름과 member 확인
# model 이 가지고 있는 member(변수, 함수) 를 알고 싶다면 dir() 를 활용하자
# model 의 이름을 알고 싶다면 __name__ 변수를 사용 하자

# print(dir(oper))  -> oper 모듈의 member 확인
# print(__name__)   -> 현재 모듈의 이름

import oper

# dir() 내장함수를 사용하면 모듈에 정의되어 있는 변수, 함수 목록을 볼 수 있다.
print(dir(oper)) # 결과: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'devision', 'field1', 'field2', 'minus', 'multiply', 'sum']

# 모듈의 이름 확인
print(oper.__name__)  # 특정 모듈의 이름을 확인 / 결과: oper
print(__name__)       # 현재 나의 이름 -> 현재 실행되는 함수 / 결과: __main__


# -------------------------------------------------------------------------------------

# 요약(Summary)

# 1. 모듈은 여러 파일에서 가져다 쓸 수 있는 공통의 기능
# 2. from, import, as 등의 쓰임새에 대해서 익숙해 지자

# -------------------------------------------------------------------------------------

# 1. O.O.P. (Object Oriented Programming)

# Python 역시도 현대의 프로그램 언어처럼 OOP 를 지향한다.
# 우선 O.O.P. 가 무엇인가?
# O.O.P. 는 소프트웨어 위기(Software Crisis) 에서 부터 시작된다.
# 자동차 공장에서 자동차를 조립하듯이 프로그램을 만드는 건 어떨까?
# 누군가가 만들어 공개한 내용을 가져다 쓰면 개발 속도가 빠르지 않을까?
# 그래서 만들어 진 것이 바로 객체 지향 프로그래밍(Object Orient Programmin) 언어이다.
# 우리가 앞에서 배운 moduel 역시도 OOP 의 개념이다.
# 하지만 누군가 만든 것을 잘 가져다 쓰려면 분류가 필요하다.
# 그래서 package와 class 라는 분류(classification) 체계가 존재한다.
# Class 는 각종 function 와 변수 등을 담는 분류(classification) 이다.
# 그러므로 class 의 이름은 어떤 변수와 함수의 종류를 대변하는 이름이어야 한다.

# -------------------------------------------------------------------------------------

# 2. Class 선언과 사용
# 첫 글자는 대문자
# 특수문자는 사용X
# 사용은 아래와 같이 특정한 변수에 넣은 후 사용 할 수 있다.
# std = Student()

# java 에서는 파일명 == 클래스명
# 파이썬에서는 꼭 그렇지 않다.
class Student: # Student 라는 클래스(학생과 관련된 함수 및 연수가 들어오겠구나 라고 예측 가능)
    pass

# Class 의 특정 내용을 사용하기 위해서는 class 를 객체화(instance) 해야 한다.
# "객체화" 란 원본 class 를 복사해 오는 것을 의미한다.
std1 = Student()
std2 = Student()
std3 = Student()

# 일련번호가 서로 다르다.
# 파이썬에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
print(std1)
print(std2)
print(std3)

# -------------------------------------------------------------------------------------

# 요약(Summary)
# 1. Class 는 classification 의 약자로 구분을 의미한다.
# 2. Class 이름은 보통 안에 있는 함수들을 대표하게 된다.
# 3. 객체화는 class 를 복사하는 것과 같다.

# -------------------------------------------------------------------------------------

# Class 의 member

# Class 안에는 여러가지들이 들어있는데 그것들을 우리는 class member 라고 부른다.
# Member 에는 constructor, variable, function 이 있다.

# 예시
# class Ex01 :            -> 클래스
#     fildName            -> 필드 == 클래스 안에 있는 변수
#     def__init__(self):  -> 생성자(생략 할 수 있다.)
#     def functionName(): -> 함수

# 생성자(construction) 는 class 를 객체화 해준다.

class Robot:

    # 생성자? 객체화 할때 호출되는 함수의 일종으로
    # 객체화가 될때 가장 먼저 호출된다.
    def __init__(self):
        print('Robot 이 복사될때 제일 먼저 호출되는 멤버')

    def doIt(self):
        print('나는 Robot 의 함수입니다.')


robot = Robot()  # ???
robot.doIt()  # ???


# 객체화 하는 과정을 다시 들여다 보면 생성자가 사용 되었다는 것을 알 수 있다.
# robot = Robot() 에서 "Robot()" 은 기본 생성자이다. ???
# Class 가 instance 화 되면서 가장 먼저 실행된다고도 볼 수 있음
# 객체화 요청 -> 생성자 호출 -> 객체화
# 생성자는 객체화 될 때 "초기화" 하는 수단으로 활용된다.
# 초기화는 0을 만드는 것이 아니고 "최초의 값"을 주는 것 이다.

# Puppy 를 객체화 할 때 이름과 목적을 주어서 초기화 해보자
class Puppy:
    name = ""  # 멤버 변수(필드) : class 안에서 사용 가능한 변수
    goal = ""

    def __init__(self, name, goal):  # 생성자 : 객체화시 호출되는 함수
        # 받아온 name 과 goal 은 이 생성자를 벗어날수 없다.
        # 그래서 클래스(객체) 멤버 에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능하다.
        # 그런데 name = name 형태로는 어떤것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀셕은 self 를 이용하여 표시해 준다.
        self.name = name
        self.goal = goal


puppy = Puppy("멍멍이", "집지키기")
print(f'이름: {puppy.name} / 목적 : {puppy.goal}')


# Class 의 객체에 접근 해당 객체의 멤버를 사용 할 수 있다.
# Car class 의 variable 과 function 을 호출 해 보자.
class Car:
    # 멤버 변수(필드)
    gear = 0
    on = False

    # 생성자
    def __int__(self):
        pass

    # 멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체들을 표시하기 위한 self 를 기본으로 가지고 있는다.
    def start(self):
        pass

    def change(self):
        pass

# -------------------------------------------------------------------------------------

# 요약(Summary)
# 1. 객체화를 할 때 constructor 라는 것을 호출한다.
# 2. Constructor 는 객체화 시에 최초로 불려진다.
# 3. 이것을 이용하면 객체화 할 경우 초기화가 가능하다.
# 4. 초기화는 생성시 최초로 어떤 값을 입력 하는 것을 의미 한다.

# -------------------------------------------------------------------------------------