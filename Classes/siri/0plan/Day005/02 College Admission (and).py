# Student must score at least 60 marks in both subjects.
maths = int(input("Maths Marks: "))
science = int(input("Science Marks: "))
chemistry = int(input("Chemistry Marks: "))

if maths >= 60 and science >= 60 and chemistry >=60:
    print("Admission Approved")
else:
    print("Admission Rejected")