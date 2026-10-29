# Exercise 3.5 - Practice: convert seconds to hours, minutes and seconds
def check(value, expected):
    print("PASS" if value == expected else f"FAIL: got {value}, expected {expected}")

total_seconds = 98765

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
check(hours, 27)
check(minutes, 26)
check(seconds, 5)
