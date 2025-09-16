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