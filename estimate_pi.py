import random

# Estimate Pi
def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        c = random.uniform(0, 1)
        q = random.uniform(0, 1)
        distance = c ** 2 + q ** 2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle / num_point_total

# print(estimate_pi(1000000))
