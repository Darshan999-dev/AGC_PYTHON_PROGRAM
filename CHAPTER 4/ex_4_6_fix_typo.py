# Exercise 4.6 - Practice: fix a typo without changing the string in place
typo = "Pxthon"

# Keep the first letter, put in the correct 'y', then keep the rest
fixed = typo[0] + "y" + typo[2:]

print("fixed:", fixed, "PASS" if fixed == "Python" else "FAIL")
