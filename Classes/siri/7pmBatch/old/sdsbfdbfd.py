class parent:
    def property(self):
        print("cash+gold+land+power")
    def marry(self):
        print("appalamma")
class child(parent):
    def marry(self):
        super().marry()
        print("kruthi")
ch=child()
ch.marry()
ch.property()