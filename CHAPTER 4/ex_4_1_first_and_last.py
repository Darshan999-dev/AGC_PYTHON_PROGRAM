# Exercise 4.1 - Warm-up: first and last
word = "Python"

first = word[0]
last = word[-1]
first_three = word[0:3]
last_three = word[-3:]

print("first:", first, "PASS" if first == "P" else "FAIL")
print("last:", last, "PASS" if last == "n" else "FAIL")
print("first_three:", first_three, "PASS" if first_three == "Pyt" else "FAIL")
print("last_three:", last_three, "PASS" if last_three == "hon" else "FAIL")
