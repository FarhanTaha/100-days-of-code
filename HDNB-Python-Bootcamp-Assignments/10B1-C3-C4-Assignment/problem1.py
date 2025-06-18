# Number Classification with Conditionals

number = int(input("Enter a number: "))

# Checking if number is zero
if number == 0:
    print("The number is zero.")

# Checking if number is positive or negative (Bonus:ternary operator)
print(f"{number} is positive." if number > 0 else f"{number} is negative.")

# Checking if number is even or odd (Personal Choice)
print(f"{number} is even." if number % 2 == 0 else f"{number} is odd")



