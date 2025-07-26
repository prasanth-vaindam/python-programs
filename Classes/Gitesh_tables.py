# print("e")
# print(size := int(input("enter a table size: ")))

for i in range(1, 11):
    for j in range(1, 13):
        # if j in [1, 2,  4, 5,  7,  8, 9, 10, 11]:
        #     continue
        print(f"{j} x {i:2d} = {i * j:3d}", end="\t")
    print()  # New line after each row of the table
