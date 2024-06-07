def len_of_str(input_str):
    count = 0
    for i in input_str:
        count += 1
    return count


while True:
    word = input("enter a string whose length you need to find: ")
    print(f"the length of the string \" {word} \" is {len_of_str(word)}")
