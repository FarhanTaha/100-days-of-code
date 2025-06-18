# PROBLEM 5

# PROBLEM 2 USING FUNCTION

def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old!")
    # Bonus
    age = int(age)
    print(f"You were {age-6} years old 6 years ago")

#calling the function
name_age()


# PROBLEM 3 USING FUNCTION

def operation():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    print(f"{num1} is greater than {num2}: {num1 > num2}")
    print(f"{num1} is equal to {num2}: {num1 == num2}")
    print(f"{num1} is less than {num2}: {num1 < num2}")

#calling the function
operation()




