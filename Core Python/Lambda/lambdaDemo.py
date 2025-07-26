def fun(*args): return sum(args)


sum_of_n_numbers = fun(1, 2, 4)
print(sum_of_n_numbers)

def fun_print(*args):
    for arg in args:
        print(arg, end=' ')

fun_print(1, 2, 3, 4, 5)
print("------>")
lambda_print = lambda *args: print(*args, end=' ')
lambda_print(1, 2, 3, 4, 5)
print("------>")

square_num = lambda x: return x * x
square_value = square_num(5)