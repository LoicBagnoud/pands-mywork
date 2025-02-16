# convert.py
# This program takes a float amount in dollars and returns that value in cent 
# author: Loic Bagnoud

amount_in_dollars = float(input("Please enter dollar amount: "))
amount_in_cents = int(round(amount_in_dollars * 100))
print(f"The amount of {amount_in_dollars} in cents is {abs(amount_in_cents)}")