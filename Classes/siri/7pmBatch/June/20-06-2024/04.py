# Convert a dictionary to a list of strings in the format "key=value".
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = [f"{k}={v}" for k, v in my_dict.items()]
print(result)
