import random

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


# Estimate Pi
def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        c = random.uniform(0,1)
        q = random.uniform(0,1)
        distance = c**2 + q**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle/num_point_total


print(estimate_pi(10000000000000))
