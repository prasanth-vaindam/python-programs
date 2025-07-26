"""
| Benefit                        | Explanation                              |
| ------------------------------ | ---------------------------------------- |
| Safer function calls           | Prevents positional argument errors      |
| More readable                  | Easier to understand what arguments mean |
| Easier to maintain             | Adding new args won't break old code     |
| Encourages explicit intent     | Reduces accidental misuse                |
| Common in libraries/frameworks | API design clarity and future-proofing   |

"""

# def process_data(data, *, normalize=False, trim=True):
#     print("Data:", data)
#     print("Normalize:", normalize)
#     print("Trim:", trim)
#
# # Example usage
# process_data([1, 2, 3], normalize=True, trim=False)
# # This function requires 'normalize' and 'trim' to be specified as keyword arguments
# # process_data([1, 2, 3], True, False)  # This would raise an error
# process_data("walla")

def process_data(data, normalize=False, trim=True):
    print("Data:", data)
    print("Normalize:", normalize)
    print("Trim:", trim)

# process_data("ok")
process_data("walla", True, False)