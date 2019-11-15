fruits = [7, 1, 3, 4, 5, 6]
colors = ["black", "yellow", "red", "blue"]
print(sorted(fruits))
# list.sort(fruits)
# print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(colors, reverse=True, key=len))
print(sorted(colors, key=len))