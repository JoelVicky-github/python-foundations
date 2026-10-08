## Block 2 — Independent discount-calculator challenge

price = 150
quantity = 1
discount_rate = 0

sub_total = price * quantity
discount_amount = sub_total * discount_rate
final_price = sub_total - discount_amount

print("\n\nPrice:", price)
print("Quantity:", quantity)
print("Sub Total:", sub_total)
print("Discount:", discount_amount)
print(f"Final price: ₹{final_price:.2f}")

