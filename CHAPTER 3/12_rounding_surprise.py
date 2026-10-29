#  Python rounds halves to the nearest even number
print(round(0.5), round(1.5), round(2.5), round(3.5))

from decimal import Decimal, ROUND_HALF_UP
print(Decimal("2.5").quantize(Decimal("1"), rounding=ROUND_HALF_UP))

print(round(2.675, 2))
