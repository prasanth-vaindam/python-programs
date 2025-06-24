b = "Hello, World!"
print(b[1:3])  #
print(b[:4])   #
print(b[3:])   #
print(b[1:1])  #

# Negative Indexing
print(b[-5:-2])  #
print(b[:])  # start from the beginning and go till the end, one step ahead
# sequence[start:stop:step]
# start: The index to begin from (inclusive).
# stop: The index to end at (exclusive).
# step: How many indices to jump forward or backward.
# all these three values are optional

word = "apple"

rWord = word[::-1]
# Step -1 (go backwards one character at a time).
# because start and stop are omitted it means it starts from the end till the beginning

# Normal Copy
sWord = word[::1]

s = "abcdef"
print(s[::1])
print(s[::2])  # Take every second character
print(s[::-1])
print(s[1:5:2])
print(s[:3])
print(s[3:])

