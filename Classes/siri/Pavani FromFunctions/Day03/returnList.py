def get_list():
    numbers = []
    def inner(n):
        numbers.append(n)
        return numbers
    return inner

insert = get_list()
insert(1)
insert(12)
print(insert(123))


