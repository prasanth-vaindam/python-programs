temp = int(input("Enter temperature: "))

result = "Hot" if temp > 35 else "Warm" if temp >= 20 else "Cold"

print(result)