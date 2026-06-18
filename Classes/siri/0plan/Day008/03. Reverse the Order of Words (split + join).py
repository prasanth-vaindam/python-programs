sentence = input("Enter a sentence: ")

words = sentence.split()

result = " ".join(words[::-1])

print(result)