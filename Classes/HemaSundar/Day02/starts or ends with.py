sen = "python is awesome"
sen2 = "i love Python"
word = "python"
if sen2.lower().startswith(word) or sen2.lower().endswith(word):
    print(f"the given sentence starts or ends with the word {word}")