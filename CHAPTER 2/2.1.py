#computing a price
price = 24.50
quantity = 3
tax_rate = 0.2

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)
