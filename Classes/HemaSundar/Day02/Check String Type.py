sen = "abc"
print(sen.isupper()) # false
print(sen.islower()) # true
print(sen.isdigit()) # false
sen = "abc123"
print(sen.isalnum()) # true
print(sen.isprintable()) # true
sen = "hello\nworld"
print(sen.isprintable()) # false
sen = "$_123Number"
print(sen.isidentifier()) # false
sen = "\t"
print(sen.isspace()) # false
sen = "émail"
print(sen.isascii()) # false

