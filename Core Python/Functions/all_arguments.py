def f_fixed(a, b, c=1, d=2):
    return a + b + c + d

def f_varargs(*args):
    return sum(args)

def f_kwargs(**kwargs):
    return sum(kwargs.values())

def f_all_args(a, b, c=1, d=2, *args, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total

def f_mixed(a, b, *args, c=1, d=2, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total

def f_mixed_with_defaults(a, b, c=1, d=2, *args, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total

def f_mixed_with_varargs(a, b, *args, c=1, d=2, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total
def f_mixed_with_kwargs(a, b, c=1, d=2, *args, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total

def f_mixed_with_all_args(a, b, c=1, d=2, *args, **kwargs):
    total = a + b + c + d
    total += sum(args)
    total += sum(kwargs.values())
    return total

f_kwargs(x=10, y=20, z=30)  # Example call to f_kwargs

f_mixed_with_kwargs(a=5, b=10, c=3, d=4, x=10, y=20)  # Example call to f_mixed_with_kwargs
f_mixed_with_all_args(1, 2, 3, 4, 5, 6, x=10, y=20)  # Example call to f_mixed_with_all_args
f_mixed_with_all_args(1, 2, 3, 4, 5, 6, x=10, y=20, z=30)  # Example call to f_mixed_with_all_args with more kwargs
