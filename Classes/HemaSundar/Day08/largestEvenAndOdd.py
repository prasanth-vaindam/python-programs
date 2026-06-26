numbers = [10,2,6,64,8,56,7,9]
numbers.sort(reverse=True)

# [64,56,10,9,8,7,6,2]
foundEven = False
foundOdd = False
for i in numbers:
    if i%2==0:
        if not foundEven:
            print("Largest Even number: ",i)
            foundEven = True
        if foundOdd:
            break
    if i%2!=0:
        if not foundOdd:
            print("Largest odd number ",i)
            foundOdd = True
        if foundEven:
            break