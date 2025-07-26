"""

I need to read and store information of the student, their name and skills
they have,
the recruiter need to sort the students based on the top
matching skills with at least minimum of 2 matching skills
w has the following skills -> ['c', 'c', 'c', 'c']
q has the following skills -> ['b', 'c', 'c']

"""



student = {
    "ravi": ['c', 'java', 'python'],
    "Ganesh": ['c', 'HTML', 'CSS', 'C++'],
    "avinash": ['c', 'java', 'python', 'C++', 'HTML', 'CSS', 'JS'],
    "naveen": ['c', 'OOP', 'Cross-Compilation'],
    "nancy": ['c'],
    "John": ['english', 'rhymes']
}

required_students = dict()

requiredSkills = ['c', 'c++', 'java', 'python', 'HTML', 'CSS', 'JS', 'Mongo DB', 'SQL']

for each_student, skills in student.items():
    count = 0
    for skill in skills:
        if skill in requiredSkills:
            count += 1

    required_students[each_student] = count


print(required_students)
required_students = sorted(required_students.items(), key=lambda x: x[1], reverse=True)
print(required_students)
for each_student in required_students:
    if each_student[1] > 1:
        print(each_student[0], " has the following skills ---> ", student[each_student[0]])
