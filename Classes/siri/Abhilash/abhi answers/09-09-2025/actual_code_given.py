class ibs:
    fine_1 = 5000#class variable

    def _init_(self, enroll_no, course, year, fine):
        self.enroll_no = enroll_no
        self.course = course
        self.year = year
        self.fine = fine

    def fine_of_std(self):
        print(
            f"the fine list for student {self.enroll_no} of year {self.year} is {self.fine_1} for not taking the leave form and the fine is placed for damaging property is {self.fine}")

    def total(self):
        return self.fine_1 + self.fine


abhi = ibs("24stuchh010639", "ai&ds", " 2", "0")# instance variable
abhi.fine_of_std()
print(" the total fine is:", abhi.total)
khaja = ibs("24stuchh010725", "ai&ds", " 2", "10000")
khaja.fine_of_std()
print(" the total fine is:", khaja.total)
mourya = ibs("24fmuchh010999", "mba", " 2", "5000")
mourya.fine_of_std()
print(" the total fine is:", mourya.total)
