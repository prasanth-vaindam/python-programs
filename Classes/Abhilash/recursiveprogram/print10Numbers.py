def numbers(i):
    i = i + 1
    print(i)
    if i == 10:
        return
    numbers(i)


numbers(0)
