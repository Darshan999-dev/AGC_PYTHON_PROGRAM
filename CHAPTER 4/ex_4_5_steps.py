# Exercise 4.5 - Practice: steps
alphabet = "abcdefghijklmnopqrstuvwxyz"

every_other = alphabet[::2]
last_five_reversed = alphabet[-1:-6:-1]

print("every_other:", every_other, "PASS" if every_other == "acegikmoqsuwy" else "FAIL")
print("last_five_reversed:", last_five_reversed, "PASS" if last_five_reversed == "zyxwv" else "FAIL")
