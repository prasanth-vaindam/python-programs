for num in range(2, 101):
    prime = True
    i = 2

    while i <= num // 2:
        if num % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(num)
        # print("Prime")
