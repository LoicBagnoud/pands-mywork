# courselist.py
# This program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data.
# author: Loic Bagnoud


# First version
'''
name_to_search_for = input("What student are you searching for? ")



student = [{
    "name" : "Mary",
    "Modules" : [
        {"Course name" : "Programming", 
         "Grade" : 45},

        {"Course name" : "History",
         "Grade" : 99}
    ]
},
{
    "name" : "John",
    "Modules" : [
        {"Course name" : "Programming", 
         "Grade" : 65},

        {"Course name" : "History",
         "Grade" : 98}
    ]
}
]

found = False


for current_student in student:
    if name_to_search_for == current_student["name"]:
        print(f"Student: {current_student['name']}")
        for module in current_student["Modules"]:
            print(f"\t{module['Course name']} \t: {module['Grade']}")
        found = True
        break

if not found:
    print("No student found in the database")
'''

# Version to account for user error

# Make the dictionaries
student = [
    {
        "name": "Mary",
        "Modules": [
            {"Course name": "Programming", "Grade": 45},
            {"Course name": "History", "Grade": 99}
        ]
    },
    {
        "name": "John",
        "Modules": [
            {"Course name": "Programming", "Grade": 65},
            {"Course name": "History", "Grade": 98}
        ]
    }
]

# Asks the user to search for the name
name_to_search_for = input("What student are you searching for? ")

# Initialize a flag to track whether the student is found
found = False

# Main loop to check the student's name
while not found:
    for current_student in student:
        if name_to_search_for == current_student["name"]:
            print(f"Student: {current_student['name']}")
            for module in current_student["Modules"]:
                print(f"\t{module['Course name']} \t: {module['Grade']}")
            found = True
            break  # Exits the loop once the student is found
    
    if not found:  # If no student is found, asks for input again
        print("No student found in the database")
        name_to_search_for = input("What student are you searching for? ")
