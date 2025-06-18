# Problem 3: For Loop Practice

list_of_numbers = [1, 2, 3, 4, 5]
list_of_squared_numbers = []

# Using a for loop to print the square of each number
print("Printing all the squares of the numbers in the List") 
for number in list_of_numbers:
    square = number ** 2
    print(f"The square of {number} is {square}")
    list_of_squared_numbers.append(square)

# Bonus: Printing only even squares
print("Printing only squares of the EVEN numbers in the List")    
for num in list_of_numbers:  
    # Printing only even squares
    if num % 2 == 0:
        sqr = num ** 2
        print(f"The square of {num} is even: {sqr}")

