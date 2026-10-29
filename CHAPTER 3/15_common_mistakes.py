# - Common mistakes, shown safely with try/except

# 1. Division by zero
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)

# 2. ^ is not power in Python (it is bitwise XOR)
print(2 ^ 3)     
print(2 ** 3)    

# 3. Implied multiplication is not allowed.
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")      
    try:
        exec("print(2(3 + 4))")
    except TypeError as error:
        print("TypeError caught:", error)

# 4. Division always gives a float
people = 12
groups = people / 4
print(groups)            
print(people // 4)       

# 5. Leading zeros are not allowed in Python 3
try:
    compile("print(007)", "<example>", "exec")
except SyntaxError as error:
    print("SyntaxError caught:", error.msg)
