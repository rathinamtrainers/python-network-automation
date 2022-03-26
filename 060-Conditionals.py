age = int(input("Enter your age: "))

if age >= 18 and age < 35:
    print("You are eligible to vote")
    print("but not eligible for contesting")
elif age >= 35:
    print("You are eligible to vote")
    print("and eligible for contesting")
else:
    print("You are not eligible to vote")
    print("and not eligible for contesting")

