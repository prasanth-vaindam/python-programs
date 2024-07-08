first_name = "pranavi"
surname = "musuku"

full_name = first_name + " " + surname
print(full_name)

print(len(surname)-1)  # 5

print(surname[len(surname)-1])  # u
print(surname[-1])  # u

# slicing

print("Mom " * 5)  #
print((first_name+" ") * 3)  #  pranavi pranavi pranavi

i = "abcdefghijklmno"
# start index to  till the end index excluding it ( end index - 1)
print(i[0:5])  # abcde

S = "Pranavi"

print(S[0:5]) 		 # Prana
print(S[1:40]) 		 # Prana
print(S[1:]) 		 # Prana
   	 # ranavi
        	 # if we don’t specify the end index - it means till the end
                          # ranavi

print(S[:4])      	 # Pran
print(S[:])