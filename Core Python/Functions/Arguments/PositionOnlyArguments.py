# Avoid conflict with existing variable names


def keyword(name, /, **kwargs):
    """
    This function demonstrates the use of a keyword-only argument.

    :param name: The name to be processed, which is a positional-only argument.
    :param kwargs: Additional keyword arguments that can be passed.
    """
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    """ suppose for suppose we have a keyword argument whose name is name, then it will not conflict"""
def add(x, y, /):
    """
    Adds two numbers together. The parameters x and y are position-only.

    :param x: The first number to add.
    :param y: The second number to add.
    :return: The sum of x and y.
    """
    return x + y

