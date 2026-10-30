# Notebook 04 - Common mistakes, shown safely with try/except

# 1. Adding a number to a string
age = 30
try:
    print("I am " + age + " years old")
except TypeError as error:
    print("TypeError:", error)
print("I am", age, "years old")                 # fix 1: commas in print()
print("I am " + str(age) + " years old")        # fix 2: convert with str()

# 2. Off-by-one in slices: length of text[a:b] is b - a
word = "Python"
print(word[1:4], len(word[1:4]))                # yth 3
print(word[1:5], len(word[1:5]))                # ytho 4

# 3. First character is index 0, last is index -1
print(word[0], word[-1])                        # P n

# 4. len needs brackets to give the answer
print(len(word))                                # 6

# 5. A string cannot be multiplied by a decimal
try:
    print(" " * 2.5)
except TypeError as error:
    print("TypeError:", error)

# 6. Expecting a string to change
word = "Python"
word + "!"                  # creates a new string, then throws it away
print(word)                 # Python
word = word + "!"           # keep it this time
print(word)                 # Python!

# Index out of range: "Python!" has indices 0 to 6, so 7 fails
try:
    print(word[7])
except IndexError as error:
    print("IndexError:", error)
