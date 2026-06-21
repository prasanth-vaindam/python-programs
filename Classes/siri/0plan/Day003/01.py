"""
Program 1: Calculate Total and Average Marks

Question:
Write a Python program to accept marks of three subjects as input.
The inputs are received as strings.
Convert them into integers, calculate the total and average, and display the results.
"""

# Accept marks
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

# Calculate
total = m1 + m2 + m3
average = total / 3

# Display
print("\n----- Result -----")
print("Total   :", total)
print(f"Average :{average:.2f}")