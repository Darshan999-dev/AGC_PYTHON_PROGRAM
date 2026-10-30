# Notebook 04 - Steps: text[start:stop:step]
word = "Python"
digits = "0123456789"
print(digits[::2])      # every second character: 02468
print(digits[1::2])     # every second, starting at index 1: 13579
print(digits[::3])      # 0369

# A negative step walks backwards
print(digits[::-1])     # 9876543210
print(word[::-1])       # nohtyP
