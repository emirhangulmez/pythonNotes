# Python Refreshing - Functions
# Author: Emirhan Gulmez

# Ranges
rangedList = list(range(50, 60))
x = len(rangedList)
while x > 0:
    text = f"Index: {len(rangedList) - x}", f"Number: {rangedList[len(rangedList) - x]}"
    x -= 1
index = 0

# Enumerate
for element in enumerate(rangedList):
    text = f"{element}"

for (index, number) in enumerate(rangedList):
    text = f"Index: {index}", f"Number: {number}"

nameList = []
name = "emirhangulmez"

for names in name:
    nameList.append(names)  # ['e', 'm', 'i', 'r', 'h', 'a', 'n', 'g', 'u', 'l', 'm', 'e', 'z']

# One Liner
nameList = [element for element in name]  # (there is same but one line)


# Functions
def math(n, q):
    return n * q


def defaultValueFunction(name="emirhan"):
    return name


defaultValueFunction()
