# Exercise 3.6 - Practice: compound interest
def check(value, expected, tol=0):
    ok = abs(value - expected) <= tol if tol else value == expected
    print("PASS" if ok else f"FAIL: got {value}, expected {expected}")

principal = 1000
rate_percent = 5
years = 10

# Method 1: formula
amount = round(principal * (1 + rate_percent / 100) ** years, 2)
print("Amount after 10 years:", amount)
check(amount, 1628.89)

# Method 2: year by year, no rounding
balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
print("Balance after 3 years:", balance)
check(balance, 1157.625, tol=1e-6)
