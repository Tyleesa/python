import numbers


numbers_a = [1, 5, 5, 6]
uniques = []

for number in numbers_a:
    if number not in uniques:
        uniques.append(number)

print(f"numbers = {numbers_a}")
print(f"uniques = {uniques}")
