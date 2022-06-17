import random

# Python Refreshing
# Author: Emirhan Gulmez
x = 1
y = random.randrange(1, 1000)
print(y)

while x < 2:
    print(type(x))
    x += 1

name = "Emirhan Gulmez"
print(name[8])
print(len(name))

# Slicing

print(name[1::])
print(name[::-1])
temp = name.split()
print(temp[1])
# Collectıons

# Lists
myList = [1, 2, 3, 4, 5, 6]

mySecondList = list()
mySecondList.append('a')
mySecondList.append('b')
print(mySecondList)
myMixedList = [0, True, 'emirhan', 0.5, 1000]
print(type(myMixedList[1]))
myNestedList = [0, 1, 2, 3, [1, True], 12.0]
print(myNestedList[4][1])

element = input("Enter a number:")
print(element.isspace())
if element.isnumeric():
    number = int(element)
    print(number + 1000)
else:
    print("Please enter the integer!")


# Dictionary (key-value-pairing)
myDictionary = {'elma':100,"banana":200}
print(myDictionary['elma'])
myDictionary["apple"] = 200
dict = myDictionary.get("emirhan",0)
print(dict)
myDictionary.pop("banana")
dict_items = myDictionary.items()
dict_values = myDictionary.values()
print(dict_values)

# Set

mySet = {1, 1, 1, 1, 1, 1, 2}
print(mySet)

myTuple = (1, 1, 2, 3, 4, 5, 6, 7, 8)
# :name_badge:
# myTuple[0] = 1
print(myTuple.count(1))

(a,b) = (1,2)
print(a)
print(b)

(a,b) = (b,a)
print(a)
print(b)