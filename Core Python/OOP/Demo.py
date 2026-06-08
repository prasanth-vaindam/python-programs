class Exam:
    def __init__(self,passMark):
        if passMark > 35:
            self.passMark = passMark
        else:
            print("Passmark can't be less than 35")


obj1 = Exam(20)
# print(obj1.passMark)
