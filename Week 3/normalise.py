# normalise.py
# This program reads in a string and strips any leading or trailing spaces, and also converts the string to lower case.
# Lastly, it outputs the length of input and output strings. 
# author: Loic Bagnoud

string_to_input = input("please enter a string: ")
normalised_string = string_to_input.strip().lower()


lenght_of_string_to_input = len(string_to_input)
lenght_of_normalised_string = len(normalised_string)

print(f"That String normalised is :{normalised_string}")
print(f"We reduced the input string from {lenght_of_string_to_input} to {lenght_of_normalised_string} characters")