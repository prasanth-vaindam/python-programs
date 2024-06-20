with open("file.txt", "r") as f:
    lines = 0
    for line in f:
        lines = lines + 1

print("No of lines in the file are ", lines)
