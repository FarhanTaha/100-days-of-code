# Problem 9: List Comprehension

mainList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to create a new list of their squares.
squareList = [x**2 for x in mainList]
print(squareList)

# Using list comprehension to filter out even numbers.
evenList = [y for y in mainList if y % 2 == 0]
print(evenList)

# Bonus: Print the sum of the squared list using sum()
print(f'Sum of all the items in the "squareList" is: {sum(squareList)}')

