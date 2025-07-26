# fun = lambda a, n: a * n
# x = fun(2, 3)
# print(x)


# Path of execution
def myfunc(n):
  return lambda a: a * n

myTripler = myfunc(3)

print(myTripler(3))

# ----
names = ['Abhi', 'Rita', 'Zoya', 'Mira']
sorted_names = sorted(names, key=lambda name: name[1])  # sort by last letter
print(sorted_names)