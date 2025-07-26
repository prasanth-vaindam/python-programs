def q():
    return 1, 2, 3, ["a", "b", "c"]


# Example usage
a, b, *c = q()
print(a, b, c)  # Output: (1, 2, 3)
