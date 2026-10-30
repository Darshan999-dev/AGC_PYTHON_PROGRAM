# Exercise 4.8 - Stretch: the middle character
s = "abcdefghi"

middle = s[len(s) // 2]
outer_removed = s[1:-1]

print("middle:", middle, "PASS" if middle == "e" else "FAIL")
print("outer_removed:", outer_removed, "PASS" if outer_removed == "bcdefgh" else "FAIL")
