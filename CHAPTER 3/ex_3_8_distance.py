# Exercise 3.8 - Stretch: distance between two points
import math

def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

x1, y1 = 1, 2
x2, y2 = 4, 6

# Using ** and math.sqrt
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance (sqrt):", distance)
check(distance, 5.0)

# Bonus: using math.hypot
distance_hypot = math.hypot(x2 - x1, y2 - y1)
print("Distance (hypot):", distance_hypot)
check(distance_hypot, 5.0)
