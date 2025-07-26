
required_skills=['c','c++','java','python']
students_dict=dict()
required_dict=dict()
name_of_skills=[]
for i in range(3):
    required_list = []
    name_of_skills=[]
    name_of_student=input("enter your name:")
    nos=int(input("enter number of skills:"))
    for j in range(nos):
        student_skill=input("enter your skills:")
        name_of_skills.append(student_skill)
    print(name_of_skills)
    students_dict[name_of_student] = name_of_skills
    for rs in required_skills:
        for s in name_of_skills:
            if rs==s:
                required_list.append(rs)
    print(required_list)
    required_dict[name_of_student]=required_list
print(students_dict)
print(required_dict)
print("--->", required_dict.items())
res = {}
res_val = []
iterationIndex = 1
for k, v in required_dict.items():
    res_val.append(len(v))
    res_val.append(v)
    res[k] = res_val
    print(iterationIndex, f" iteration key value is {k} and value is {res[k]} --- {res_val} ", res)
    iterationIndex += 1
    res_val = []  # why is the res_val not being updated for the key in first iteration to empty list because i am just putting res[k] = res_val in two lines above


print(res)

