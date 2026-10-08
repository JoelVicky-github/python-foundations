# Exercise 1: Arithmetic operations

print("\nExercise 1: Arithmetic operations\n")

number_one = 20
number_two = 6

print("Addition:", number_one + number_two)
print("Subtraction:", number_one - number_two)
print("Multiplication:", number_one * number_two)
print("Normal division:", number_one / number_two)
print("Floor division:", number_one // number_two)
print("Remainder:", number_one % number_two)
print("Exponent:", number_one ** number_two)


# Exercise 2: Rectangle calculator

print("\nExercise 2: Rectangle calculator\n")

length = 7
width = 3

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


# Exercise 3: Temperature converter

print("\nExercise 3: Temperature converter\n")

celsius = 100
fahrenheit = (celsius * 9) / 5 + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)


# Exercise 4: Bill calculator

print("\nExercise 4: Bill calculator\n")

item_price = 250
quantity = 3
tax_rate = 0.18

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Item price: ₹{item_price:.2f}")
print("Quantity:", quantity)
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax: ₹{tax:.2f}")
print(f"Final total: ₹{total:.2f}")
