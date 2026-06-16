data = "mango,apple,banana"
list_of_words = data.split(",")
print(list_of_words)

joined = ",".join(sorted(list_of_words))
print(joined)
print(sorted(list_of_words))