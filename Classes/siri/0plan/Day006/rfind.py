text = "banana"

print(text.find("a"))
print(text.rfind("a"))

text = "one two one two one two"

print("position of two",text.rfind("two",0,19))

text = "bananaa"

print(text.rfind("a", 0, 6))
print(text.rfind("a", 0, 5))
print(text.rfind("a", 0, 4))