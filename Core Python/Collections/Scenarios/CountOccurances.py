numbers = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]

occurrencesCount = {}

for number in numbers:
    if number not in occurrencesCount.keys():
        occurrencesCount.update({number: 1})
    else:
        # count = occurrencesCount[number]
        # occurrencesCount.update({number: (count + 1)})
        occurrencesCount.update({number: occurrencesCount[number] + 1})

print(occurrencesCount)


# for number in numbers:
#     occurrencesCount[number] = occurrencesCount.get(number, 0) + 1
#
# for key, value in enumerate(occurrencesCount):
#     print(f"the number {key} is present {value} time(s)")
