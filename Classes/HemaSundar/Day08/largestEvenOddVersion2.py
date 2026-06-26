numbers = [10,2,6,64,8,56,7,9]

even = []
odd = []
for i in numbers:
    if i%2==0:
        even.append(i)

    if i%2!=0:
        odd.append(i)

even.sort(reverse=True)
odd.sort(reverse=True)
print("Largest even number: ", even[0])
print("Largest odd number: ", odd[0])