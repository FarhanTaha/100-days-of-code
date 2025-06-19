# Problem 1: Write Dictionary Data to a Text File

# Creating dictionaries for person, product, and grades
person = {
    "name": "Jahid",
    "age": 30,
    "city": "Jessore"
}

product = {
    "id": "SKU12345",
    "name": "Wireless Mouse",
    "price": 1200,
    "in_stock": True
}

grades = {
    "student": "Samin",
    "math": 85,
    "science": 90,
    "english": 88
}

# Writing the dictionaries to the same text file
with open("data.txt", "w") as f: # Using with statement so file.close() automates
    f.write("[Person Info]\n")
    for key, value in person.items():
        f.write(f"{key}: {value}\n")
    
    f.write("\n[Product Info]\n")
    for key, value in product.items():
        f.write(f"{key}: {value}\n")
    
    f.write("\n[Student Grades]\n")
    for key, value in grades.items():
        f.write(f"{key}: {value}\n")

