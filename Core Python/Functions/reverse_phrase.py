# Program to reverse a phrase
# Is String Mutable

def reverse_phrase(input_word):
    word = list(input_word)
    print("In Function: ", word)
    i = 0
    j = len(word) - 1
    temp = ''

    while i < j:
        temp = word[i]
        word[i] = word[j]
        word[j] = temp
        i = i + 1
        j = j - 1

    input_word = ''.join(word)
    return input_word


print(reverse_phrase(input("Enter a Phrase to reverse: ")))


