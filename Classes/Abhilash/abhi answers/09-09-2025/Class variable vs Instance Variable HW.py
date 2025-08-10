# program to print the difference between Class Variable and Instance Variable
# Note the Changes I have made, Naming Conventions are important,
# Presentation is also very important it helps in readability of code and Output
# it took 30 minutes for refactoring this simple program don't repeat the mistakes
# HW: Try to improve further and compare and contrast with your code

class Ibs:
    leaveFrom_missing_fine = 5000  # class variable

    def __init__(self, enroll_no, course, year, fine):
        self.enroll_no = enroll_no
        self.course = course
        self.year = year
        self.damaging_property_fine = fine

    def fine_of_std(self):
        print(
            f"the fine list for student  bearing roll number {self.enroll_no} and "
            f"of year {self.year} is \n"
            f"1. {self.leaveFrom_missing_fine} for not taking the leave form and the fine is placed\n"
            f"2. {self.damaging_property_fine} for damaging property\n")

    def total(self):
        t = Ibs.leaveFrom_missing_fine + self.damaging_property_fine
        print(f"-->Help here: {t}")
        # print(Ibs.leaveFrom_missing_fine + )


student_One = Ibs("24stuchh010639", "ai&ds", "2", 0)  # instance variable
student_One.fine_of_std()
student_One.total()

student_two = Ibs("24stuchh010725", "ai&ds", "2", 10000)
student_two.fine_of_std()
student_two.total()

student_three = Ibs("24fmuchh010999", "mba", "2", 5000)
student_three.fine_of_std()
student_three.total()
