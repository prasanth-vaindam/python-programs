nums = [1, 2, 3, 4, 5]


# This code filters even numbers from a list using a lambda function.
def isEven(x):
    return x % 2 == 0


even_nums = list(filter(isEven, nums))
print(even_nums)

squared = list(map(lambda x: x * x, nums))
print(squared)

# even_nums = list(filter(lambda x: x % 2 == 0, nums))

from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)
# from typing import Callable, List, Any
# from operator import add, mul
# def apply_function_to_list(func: Callable[[Any], Any], lst: List[Any]) -> List[Any]:
#     """Applies a function to each element in the list."""
#     return list(map(func, lst))
