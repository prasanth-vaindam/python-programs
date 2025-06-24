# built in functions

# letter = "a"
# print("1 ", letter.isalpha())  # True
# print("2 ", letter.islower())  # True
# print("3 ", letter.lower())  # a
# print("4 ", letter.upper())  # A
# letter = letter.upper()
# print("5 ", letter.isupper())  # False
#
letter = "asdfgmn34897+++"
print("6 ", letter.isalnum())  # True
letter = "jkh34897"
print("7 ", letter.isnumeric())  # False
letter = "aslfkdj@#!%$~"
print("8 ",letter.isascii())  # True american standard code for information interchange
letter = "rasanth dfj\n \tkl)dskjgvaindamsd.zfkjalkdfjklj"
print(letter)
letter = " "
print("9 ", letter.isprintable()) #
print("10 ", letter.isspace())   # False
letter = "Prasanth Vaindam Dsalkj"
print("11 ", letter.istitle())
letter = "1"
print("12", letter.isdigit())
letter = "1Prasanth_Is_a1"
print("13", letter.isidentifier())

