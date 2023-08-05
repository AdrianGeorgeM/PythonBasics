# Sorting Lists

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
items.sort()
print(items)

items.sort(reverse=True)  # sort in reverse order
# print(items)

items = [
    "dog",
    "cat",
    "fish",
    "zebra",
    "ape",
    "lion",
    "cow",
    "antelope",
    "moose",
    "aardvark",
]
# items.sort()  # sort alphabetically
# print(items)

# items.sort(key=len)
# print(items) # sort by length of string in list item (shortest to longest)
# itemsCopy = items[:]  # copy list
# items.sort(key=str.lower)
# print(items)  # sort alphabetically, ignoring case
# print(itemsCopy)  # print original list
sortedItems = sorted(
    items
)  # sort list and save to new variable create new list without changing original list
print(sortedItems)  # print sorted list
