# Program to reverse a Phrase
# String are immutable cannot be changed inplace

def reverse_phrase(phrase):
    i = 0
    j = len(phrase) - 1
    word = list(phrase)

    temp = ''
    while i < j:
        temp = word[i]
        word[i] = word[j]
        word[j] = temp
        i = i + 1
        j = j - 1

    reverse = ''.join(word)
    print(reverse)


# reverse_phrase("pot")
while True:
    reverse_phrase(input("Enter a Phrase to reverse it: "))
