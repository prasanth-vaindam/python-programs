for i in range(5):
    for j in range(5):
        if (i+j) %2 == 0:
            print("X", end="")
        else:
            print("O",end="")
    print()