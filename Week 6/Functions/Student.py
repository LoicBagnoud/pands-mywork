# Student.py
# This program  program that allows a user to create new students and to view students
# author: Loic Bagnoud

import json

# List to store students
students = []


# Function to display the main menu
def display_menu():
    print("What would you like to do?")
    print("\t (a) Add new Students")
    print("\t (v) View Students")
    print("\t (s) Save Students")
    print("\t (l) Load Student File")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/s/l/q:): ")
    return choice

# Function to add students
def Add():
    current_student = {}
    current_student ["Name"] = input("Enter name: ")
    current_student ["Modules"] = read_modules()

    students.append(current_student)

# Function to add Modules
def read_modules():
    modules = []
    module_name = input("\Enter the first module name (Blank to quit): ")

    while module_name != "":
        module = {}
        module ["Name"] = module_name
        module ["Grade"] = int(input("\t\tInput the Grade: "))
        modules.append(module)
        module_name = input("\t Enter the next Module name (Blank to quit): ")
    return modules

# Function to Display the Modules
def display_modules(modules):
    print("\t Name:  \t Grade:")
    for module in modules:
        print(f"\t {module['Name']}    \t {module['Grade']}")


# Function to view the students
def View():
    for current_student in students:
        print(current_student["Name"])
        display_modules(current_student["Modules"])

# Function to save students into a Json file
def do_save(obj):
    with open("students.json", 'wt') as f:
        json.dump(obj, f)
    print("Students saved")

# Function to Load json files as dictionary files
def do_load():
    try:
        with open("students.json", 'r') as f:
            data = json.load(f)
            print("Students loaded successfully.")
            return data
    except FileNotFoundError:
        print("No saved students found. Returning to main menu.")
        return []


# The actual menu with conditional branching.
# List to store students

choice = display_menu()
while(choice != "q"):
    if choice == "a":
        Add()
    elif choice == "v":
        View()
    elif choice == "s":
        do_save(students)
    elif choice == "l":
        students = do_load()
    elif choice != "q":
        print("\n\nThat was not one of the Options. \nPlease select one of the options")
    choice = display_menu()





    