choice =0

while choice !=4:
    print("1. Add")
    print("2. Remove ")
    print("3. Guess")
    print("4. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("Added")
    elif choice == 2:
        print("Removed")
    elif choice == 3:
        print("Guessed")
    else:
        print("Thanks")

print("Program ended")