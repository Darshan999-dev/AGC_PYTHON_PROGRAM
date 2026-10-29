# Exercise 3.1 - Warm-up: seconds in a week
def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

seconds_per_week = 7 * 24 * 60 * 60
print("Seconds per week:", seconds_per_week)
check(seconds_per_week, 604800)
