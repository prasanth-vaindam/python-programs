str = "banana"
print(str.find('a'))
print(str.count('a'))
first = str.find('a')
second = str.find('a',first+1)
print(second)

str = "ravi.kumar@gmail.com"
pos = str.rfind('@')
print(str[pos+1:])

print(str.__contains__('@') and str.endswith(".com"))

url = "https://www.youtube.com"

pos = url.rfind("/")+1
print(url[pos:])

sentence = "i love C# and C#"
sentence = sentence.replace("C#", "java")
print(sentence)
list_of_fruits = ["apple", "banana", "mango"]
fruits = ",".join(list_of_fruits)
print(fruits)
l_fruits = fruits.split(",")