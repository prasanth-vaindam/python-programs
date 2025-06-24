fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]

# for x in fruits:
#   if "a" in x:
#     new_list.append(x)

print(new_list)

new_list.remove("apple")
print(new_list)