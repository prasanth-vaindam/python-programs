line = "welcome took 16.42s for 8×6 (Table 8) – slow response"

table = int(
    line.strip().split("Table")[1].split(")")[0].strip()
            )
print(table)
print(line.strip().split("Table")[1])  # 8) – slow response

line = "Rohit missed: 4×4 = 16, answered: 8 (Table 4)"
table = int(
    line.strip().split("Table")[1].split(")")[0].strip()
            )
