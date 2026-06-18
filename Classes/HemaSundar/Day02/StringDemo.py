s = "banananana"

first_pos = s.find("a")
sec_pos = s.find("a", first_pos+1)
third_pos = s.find("a", sec_pos+1)
print(third_pos)
