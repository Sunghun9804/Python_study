class Runner:
    # def __init__(self):
    #     pass             ----> 생성자 생략

    def run(self):
        print(f'달린다.')

    def sprint(self):
        print(f'전력질주를 한다.')

class Jumper:
    def jump(self):
        print(f'점프를 한다.')

    def high_jump(self):
        print(f'높이 점프를 한다.')

class Person(Jumper, Runner): # jumper 와 Runner 를 상속 받았다.
    def walk(self):
        print(f'걷는다.')

# walk() 함수를 사용하기 위해 Person 클래스를 객체화 한다.
p = Person()
p.walk()

# 상속받은 함수들을 내것처럼(p객체로부터) 사용한다.
p.sprint()
p.high_jump()
p.jump()
p.walk()