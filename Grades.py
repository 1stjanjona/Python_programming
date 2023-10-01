grades = float(input("Enter your grade here:\n"))
if grades >= 90:
    print("Excellent! You have A")
elif grades < 90 and grades >= 75:
    print("Good! You have B")
elif grades < 75 and grades >= 50:
    print("Accepted! You have C")
else:
    print("Failed! You have F")
