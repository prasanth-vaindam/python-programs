# this is a program to print 5 4 3 2 1
n = int(input("enter a number "))

for i in range(0, n):
    for j in range(n - i, 0, -1):
        print(j, end="")
    print()

    # this is a program to print the numbers in a row

#
# n = #int(input( "enter a number of rows:"))
# for# i in range (1,n+1):
#  for j in range (1,n+1):
#       print(chr(64+j ) , end = "")
#
# this is a program for printing the numbers back to front like fo example 10 to 1
# n = int (input ( "enter a number :"))
# for i in range (1,n+1):
# for j in range (1,n+1):
# print ("hi hello i am d jahnavi priya of narayana school and i am studying in seventh class and in olympiad group ")
