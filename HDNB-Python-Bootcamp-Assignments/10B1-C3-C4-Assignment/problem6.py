# Problem 6: Dictionary Practice

# Create a dictionary of three students and their grades
students_name_grades = {"Taha": 92, "Talha" : 91, "Samiul" : 99}

# Update the grade of one student
students_name_grades["Taha"] = 95

# Add a new student and their grade
students_name_grades["Rafid"] = 90

# Remove a student from the dictionary
del students_name_grades["Talha"]

# Print the updated dictionary using loop
for student,grade in students_name_grades.items():
    print(f"{student} : {grade}")
 
# Bonus: Print the average grade of the students
average_grade = sum(students_name_grades.values()) / len(students_name_grades)
print(f"Average grade of all student: {average_grade:.2f}")

