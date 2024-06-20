f=open("file.txt","r")
words=0
lines=0
chars=0
for line in f:
    lines=lines+1
    chars=chars+len(line)
    words=words+len(line.split())

print(lines)
print(chars)
print(words)
