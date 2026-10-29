# Exercise 3.4 - Practice: tip calculator
def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

bill = 84.50
tip_percent = 18
people = 4

tip = bill * tip_percent / 100
total = round(bill + tip, 2)
per_person = round(total / people, 2)

print("Tip:", round(tip, 2), "| Total:", total, "| Per person:", per_person)
check(round(tip, 2), 15.21)
check(total, 99.71)
check(per_person, 24.93)
