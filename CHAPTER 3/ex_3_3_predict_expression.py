# Exercise 3.3 - Predict: 2 + 3 * 4 ** 2 / 8 - 1
# Order: 4 ** 2 = 16, then 3 * 16 = 48, then 48 / 8 = 6.0, then 2 + 6.0 - 1 = 7.0
def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

prediction = 7.0
value = 2 + 3 * 4 ** 2 / 8 - 1
print("Expression value:", value)
check(prediction, value)
check(prediction, 7.0)
