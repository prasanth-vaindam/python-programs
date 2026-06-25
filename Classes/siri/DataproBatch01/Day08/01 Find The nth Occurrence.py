s = "bananana"

first_occurrence = s.find("a")
second_occurrence = s.find("a", first_occurrence+1)
third_occurrence = s.find("a",second_occurrence+1)
print(third_occurrence)
