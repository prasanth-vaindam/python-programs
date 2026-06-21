int("9.5")       # ValueError
int("hello")     # ValueError

float("abc")     # ValueError

list(10)         # TypeError
tuple(10)        # TypeError
set(10)          # TypeError

dict("abc")      # ValueError