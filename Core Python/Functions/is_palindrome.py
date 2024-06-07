# Program to check if the given number is Palindrome
# definition of palindrome: a word, phrase, or sequence that reads the same backwards as forwards,
# e.g. madam or nurses run or 12321 pop .

def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        # Handle the case for nurses run
        if word[i] == ' ':
            i += 1
        if word[j] == ' ':
            j -= 1

        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False

    if i >= len(word) // 2:
        return True
    else:
        return False


input_word = input("Enter a  Word / Number to check if it is palindrome: ")
print(f"is_palindrome ({input_word}) : {is_palindrome(input_word)}")