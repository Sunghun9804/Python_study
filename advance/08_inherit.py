class Runner:
    # def __init__(self):
    #     pass             ----> 생성자 생략

    def run(self):
        pass

    def sprint(self):
        pass

class Jumper:
    def jump(self):
        pass

    def high_jump(self):
        pass

class Person(Jumper, Runner):
    pass