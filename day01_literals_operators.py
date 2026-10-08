"""kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")"""


### Exercise 1: Arithmetic operations
print("\nExercise 1: Arithmetic operations\n")
number_one = 20
number_two = 6

print("Addition: ",number_one + number_two)
print("Subtraction: ",number_one - number_two)
print("Multiplication: ",number_one * number_two)
print("Normal division: ",number_one / number_two)
print("Floor division: ",number_one // number_two)
print("Remainder: ",number_one % number_two)
print("Exponent: ",number_one ** number_two , "\n")


### Exercise 2: Rectangle calculator
print("Exercise 2: Rectangle calculator\n")

length = 7
width = 3

area = length * width
perimeter = 2 *(length + width)

print("Area:", area)
print("Perimeter:", perimeter, "\n")

### Exercise 3: Temperature converter
print("Exercise 3: Temperature converter")

celsius = 100
farenheit = (celsius * 9) / 5 + 32

print("Farenheit:", farenheit, "\n")

### Exercise 4: Bill calculator
print("Exercise 4: Bill calculator\n")

item_price = 250
quantity = 3
tax_rate = 0.18

sub_total = item_price * quantity
tax = sub_total * tax_rate
total = sub_total + tax

print(" Subtotal:", sub_total, "\n", "Tax:", tax, "\n", "Final_Total:", total)

