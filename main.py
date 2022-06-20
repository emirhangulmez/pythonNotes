# Python Refreshing
# Author: Emirhan Gulmez

# Variables
x = 10
y = 20
z = 30

# Other way
(a, b, c) = (10, 20, 30)
# Additional Feature
(c, b, a) = (a, b, c)

# Slicing
name = "Emirhan Gulmez"
splittedName = name.split()
lengthName = len(name)
# name[start:end:step]
# Reversing -> print(name[::-1])


# Collections
myList = [1, ['list', 1, 2], 3, 4.0, True]  # List -> Regular List

mySet = {1, 1, 2, 2, 3, 3, 4, 5}  # Set -> {1, 2, 3, 4, 5} Unique

myTuple = (1, 2, 3, 3, 4, 5)  # Tuple -> You cannot assign.
myTuple.count(3)  # 2

myDict = {1: 2, 4: 3}  # Dictionary -> Hashmap style (key-value-pairing)
myDict.get(6, 0)  # 6 is not defined -> 0
myDict.items()  # (1, 2), (4, 3)
myDict.values()  # [2,3]

# Converting data structures to each other #

# Error Handling

ageInput = 0  # input("Enter Age: ")

try:
    result = int(ageInput)
except ValueError as e:
    print(e)
    result = "An error occurred!"

# If Statement and Operators
x = 10
if 0 < x <= 30:
    text = "0 > x <= 30"
elif 30 < x <= 40:
    text = "30 > x <= 40"
else:
    text = "x > 40"

numbersList = [10, 20, 30, 40, 50]

for numbers in numbersList:
    squareOfNumbers = numbers ** 2  # Returns the all of lists items square numbers

number = 0
while number < 10:
    # 1,2,3,4,5,6,7,8,9
    number += 1

eq = "e" in "Machine"  # Return true

# Formatted String
# print(f"Your Age: {age}) or print("Your Age", age)

# Remainder
# print(10%4) # Returns 2
