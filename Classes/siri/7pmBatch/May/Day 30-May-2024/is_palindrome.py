# program to check if the given phrase is a palindrome

def is_palindrome(word):
    i = 0
    j = len(word) - 1 # because index starts from 0
    while i < j:
        if word[i] == word[j]:
            i += 1  # move i pointer towards right
            j -= 1  # move j  pointer towards left
        else:
            # print(f"No, The Given word {word} is not a palindrome")
            return False

    if i >= len(word)//2:
        # print(f"Yes, The Given phrase {word} is a palindrome")
        return True
    else:
        # print(f"No, The Given word {word} is not a palindrome")
        return False


while True:
    input_word = input("enter a phrase to check if it is a palindrome: ")
    if is_palindrome(input_word):
        print(f"The Given Phrase {input_word} is a Palindrome!")
    else:
        print(f"The Given Phrase {input_word} is Not a Palindrome!")
