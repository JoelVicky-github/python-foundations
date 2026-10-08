# Independent discount-calculator challenge

print("\nDiscount Calculator\n")

price = 500
quantity = 4
discount_rate = 0.10

subtotal = price * quantity
discount_amount = subtotal * discount_rate
final_price = subtotal - discount_amount

print(f"Price: ₹{price:.2f}")
print("Quantity:", quantity)
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount rate: {discount_rate * 100:.0f}%")
print(f"Discount amount: ₹{discount_amount:.2f}")
print(f"Final price: ₹{final_price:.2f}")
