# CTI-110 P1HW1 - Travel Expense
# A program that calculates the total amount of travel expenses.
# 04/06/2023
# Faith Rivera

# Ask user to enter their budget
budget = 1200.0

# Ask user to enter travel destination
destination = "Nashville"

# Ask user for amount they will spend on gas
gas_cost = 250.0

# Ask user for amount they will spend on accommodation
accommodation_cost = 600.0

# Ask user for amount they will spend on food
food_cost = 300.0

# Add expenses
total_expenses = gas_cost + accommodation_cost + food_cost

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\nTravel expenses for", destination)
print("Gas cost: $", format(gas_cost, ".2f"), sep="")
print("Accommodation cost: $", format(accommodation_cost, ".2f"), sep="")
print("Food cost: $", format(food_cost, ".2f"), sep="")
print("Total expenses: $", format(total_expenses, ".2f"), sep="")
print("Remaining budget: $", format(remaining_budget, ".2f"), sep="")
