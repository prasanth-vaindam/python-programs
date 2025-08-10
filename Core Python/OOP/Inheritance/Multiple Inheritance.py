class A:
    def display(self):
        print("apple")
    def amethod(self):
        print("inClass A")


class B:
    def display(self):
        print("orange")

    def bmethod(self):
        print("inClass B")


class Child(B, A):
    pass


obj = Child()
obj.display()
obj.bmethod()
obj.amethod()
