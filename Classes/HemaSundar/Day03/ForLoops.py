sentence = "apple is a fruit"
for letter in sentence:
    print(letter)

for i,letter in enumerate("ace"):
    if i==0:
        continue
    print(i,letter)

for i,num in enumerate([10,2,4,5,7,8,33]):
    if num%2==0:
        print(f"at index:{i}, {num}")

numbers = [10,2,4,5]
sum = 0
for i in numbers:
    sum += i
print("-------------------")
for i in range(1,10,-1):
    print(i)

fruits = "apple, Mango, banana"

fruits_list = fruits.lower().strip().split(",")


print("-->",fruits_list)
newList = []
for fruit in fruits_list:
    newList.append(fruit.strip())

newList = sorted(newList)
print(newList)

names = "  ram  ravi hari  gopal  "
names_list = names.split()
for name in names_list:
    print(name.strip().title())