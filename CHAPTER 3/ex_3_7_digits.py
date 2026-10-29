# Exercise 3.7 - Stretch: pull apart digits using only // and %
def check(value, expected, hint=""):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected} {hint}")

n = 4827

last_digit = n % 10
without_last = n // 10
tens_digit = without_last % 10

print("Last digit:", last_digit, "| without last:", without_last, "| tens digit:", tens_digit)
check(last_digit, 7)
check(without_last, 482)
check(tens_digit, 2, "(remove last digit first, then take its last digit)")
