# Problem 7: Tuple Slicing

myTuple = 0,1,2,3,4,5,6,7,8,9

# Printing first three items
firstThreeItems = myTuple[0:3]
print(firstThreeItems)

# Printing last three items
lastThreeItems = myTuple[7:10]
print(lastThreeItems)

# Print every second item
my2ndItemList = []
for i in range(1, len(myTuple), 2):
    my2ndItemList.append(myTuple[i])

print(tuple(my2ndItemList))

# Bonus: Trying to Mutate the tuple
myTuple[0] = 10 # TypeError: 'tuple' object does not support item assignment





