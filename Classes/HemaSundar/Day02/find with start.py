s = "one two one two one two one two one two"

first_pos = s.find("two")
print(first_pos)
sec_pos = s.find("two",first_pos+1)
print(sec_pos)
