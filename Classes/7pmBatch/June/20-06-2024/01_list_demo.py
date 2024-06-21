this_list = [1,2,3,4,5,6,7,8,9,10]

squares = [x*x for x in this_list]
print(squares)

numbers_1_to_100 = [i for i in range(1,101)]
print(numbers_1_to_100)

squares_of_numbers_1_to_100 = [i*i for i in range(1,101)]
print(squares_of_numbers_1_to_100)

print("count of this list", len(squares_of_numbers_1_to_100))

even_numbers_in = [x for x in range(1, 101) if x % 2 == 0 ]
print(even_numbers_in)
