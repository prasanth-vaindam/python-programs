tests = [
    ("isalnum", "abc123", "abc 123"),
    ("isalpha", "Python", "Python123"),
    ("isdigit", "12345", "12.34"),
    ("islower", "python", "Python"),
    ("isspace", "   ", "abc"),
    ("isupper", "PYTHON", "Python"),
    ("isnumeric", "12345", "123abc"),
    ("isdecimal", "12345", "12.5"),
    ("isidentifier", "student_name", "123name"),
    ("isprintable", "Hello123", "Hello\nWorld"),
    ("isascii", "Python123", "Pythön")
]

for name, true_str, false_str in tests:
    print("\n", name)
    print("True Example :", true_str)
    print("False Example:", false_str)