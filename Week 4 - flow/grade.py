# grade.py
# This program reads in a student’s percentage mark and prints out corresponding the grade
# author: Loic Bagnoud

percentage = float(input("Enter the percentage: "))

if round(percentage) < 0 or round(percentage) > 100:
    print(f"{percentage} is not a valid number. Please enter a valid number")

elif round(percentage) < 40:
    print("Fail")
elif round(percentage) < 50:
    print("Pass")
elif round(percentage) < 60:
    print("Merit 2")
elif round(percentage) < 70:
    print("Merit 1")
else:
    print("Distinction")