# built in functions

letter = "a"
print("1 ", letter.isalpha())  # True
print("2 ", letter.islower()) # True
print("3 ", letter.lower()) # True a | a
print("4 ", letter.upper()) #A
print("5 ", letter.isupper()) # True A| True A|False A |
letter = "asdfgmn34897+++"
print("6 ", letter.isalnum()) # True
letter = "jkh34897"
print("7 ", letter.isnumeric()) #False
letter = "aslfkdj@#!%$~"
print("8 ",letter.isascii())# american standard code for information interchange
letter = "rasanth dfj\n \tkl)dskjgvaindamsd.zfkjalkdfjklj"
# letter = ""
print("9 ", letter.isprintable())
print("10 ", letter.isspace())
letter = "Prasanth Vaindam dsalkj"
print("11 ", letter.istitle())
print("12", letter.isdigit())
letter = "Prasanth Vaindam dsalkj"
print("13", letter.isidentifier())