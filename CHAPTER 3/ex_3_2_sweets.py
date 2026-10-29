# Exercise 3.2 - Warm-up: quotient and remainder
def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

sweets = 17
children = 5

each = sweets // children
left_over = sweets % children
print("Each child gets:", each, "| left over:", left_over)
check(each, 3)
check(left_over, 2)
