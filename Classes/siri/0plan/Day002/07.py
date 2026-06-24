# set() -> converts a iterable to set
# print(set([1,1,2,2,3,3,1])) 	#{1,2,3}

# print(set("hello"))	#
print(set((1,2,3)))	#{1,2,3}
# set(10)	           #❌ TypeError

p = {}
# print(type(p))
q = set()
print(type(q))