# Lists
dogs = ["border collie", "australian cattle dog", "labrador retriever", 1, True]

print("border collie" in dogs)
print(dogs)

dogs = ["border collie", "australian cattle dog", "labrador retriever", 1, True]
print(dogs)
# dogs[0] = "australian shepherd"
print(dogs[:2])  # print first two elements
print(dogs[1:2])  # print second element
print(dogs[1:])  # print from second element to end
print(dogs[-1])  # print last element
print(dogs[-2:])  # print last two elements
print(dogs[:-1])  # print all elements except last
print(dogs[::2])  # print every other element
print(dogs[::-1])  # print list in reverse order
print(len(dogs))  # print length of list
dogs.extend(["poodle", "shiba inu"])  # add two elements to end of list
dogs += ["poodle", "golden retriever", "terrier"]  # add two elements to end of list
dogs.remove("poodle")  # remove element from list
print(dogs.pop())  # remove last element from list§ and return it
dogs.insert(0, "poodle1")  # insert element at index
dogs.sort()  # sort list
dogs[1:2] = ["poodle1"]  # insert list into list
print(dogs)
