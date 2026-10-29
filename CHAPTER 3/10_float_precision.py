# Why 0.1 + 0.2 is not 0.3
import math

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print(f"{0.1:.30f}")
print(f"{0.1 + 0.2:.30f}")

print(math.isclose(0.1 + 0.2, 0.3))
print(round(0.1 + 0.2, 2) == 0.3)

price_in_cents = 1999
print(price_in_cents * 3)
