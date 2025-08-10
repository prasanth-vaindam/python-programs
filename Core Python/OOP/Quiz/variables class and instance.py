class Counter:
    count = 0  # Class variable

    def __init__(self):
        self.count = 0  # Instance variable

a = Counter()
b = Counter()
a.count += 1
Counter.count += 10

print(a.count)  # ? 1
print(b.count)  # ? 0
print(Counter.count)  # ? 10
print(a.__dict__)  # ? {'count': 1}