num = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}

phone = input("Phone: ")
s = ""
for i in phone:
    s += num[i] + " "
print(f"{s}")
