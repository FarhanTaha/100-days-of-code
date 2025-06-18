# Problem 8: Set Operations

students_set1 = {"Rahim", "Sumon", "Akash", "Biplob"}
students_set2 = {"Akash", "Biplob", "Trisha", "Mita"}

# Union
unionSet = students_set1.union(students_set2)
print(f"Union of the sets: {unionSet}")

# Intersection
intersectionSet = students_set1.intersection(students_set2)
print(f"Intersection of the sets: {intersectionSet}")

# Difference (set1 - set2)
differenceSet = students_set1.difference(students_set2)
print(f"Difference of the sets (set1 - set2): {differenceSet}")

# Difference (set2 - set1)
differenceSet2 = students_set2.difference(students_set1)
print(f"Difference of the sets (set2 - set1): {differenceSet2}")

# Adding Elements
students_set1.add("John")
print(f"Set after adding 'John': {students_set1}")

# Removing Elements
students_set1.remove("Rahim")
print(f"Set after removing 'Rahim': {students_set1}")

# Bonus: Check if a specific name exists in the set using "in"
name_to_check = "Farhan"
if name_to_check in students_set1 or name_to_check in students_set2:
    print(f"{name_to_check} is in the sets.")    
else:
    print(f"{name_to_check} is not in the sets.")
    