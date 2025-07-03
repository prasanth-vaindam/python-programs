"""



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

for each_student, skills in enumerate(student):
    for skill in skills:
        required_students[each_student] = required_students.get(each_student, 0) + 1

print(required_students)

