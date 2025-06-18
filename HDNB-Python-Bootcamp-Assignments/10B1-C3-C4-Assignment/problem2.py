# Problem 2: Age Eligibility Check

age = int(input("Enter your age: "))

# Checking eligibility based on age & income (Bonus: Nested if-else)
if age >= 18:
    income = float(input("Enter your income: "))
    if income >= 50000:
        print("Eligible for premium membership")
    else:
        print("Eligible for standard membership")
else:
    print("Not eligible for membership")

