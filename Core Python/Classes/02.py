class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):        # Getter
        return self.__marks

    def set_marks(self, marks): # Setter
        if marks >= 0:
            self.__marks = marks

    def __str__(self):
        return f"Student(marks={self.__marks})"

    def __repr__(self):
        return f"Student(marks={self.__marks})"

    def display(self):
        print(f"Student marks: {self.__marks}")

    def display_self():
            print(f"Sleflessness")
    def geeting(self):
        print("Hello, you are calling a behaviour method of the Student class using a method call, not an attribute access through object instance.")

s = Student(88)
# print(s.get_marks())  # ✅ Clean and safe
Student.geeting(s)
Student.display_self()

 # using the self variable can i access the instance variables declared across different methods?
