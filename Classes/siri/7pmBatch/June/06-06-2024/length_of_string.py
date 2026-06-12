# Program to find the length of the String

def len_of_str(input_str):
    count = 0
    for i in input_str:
        count += 1
    return count


while True:
    word = input("Enter a word to know it's length")
    print(f"The length of the string {word} is {len_of_str(word)}")
