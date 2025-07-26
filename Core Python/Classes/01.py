class Animal:
    def __init__(me, name):
        me.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


a = Animal("Tiger")
a.speak()
