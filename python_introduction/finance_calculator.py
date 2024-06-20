# This script calculates the monthly savings and projected savings after one year with interest

# Get user input for monthly income and expenses
monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpense = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthlySavings = monthlyIncome - monthlyExpense

# Calculate projected savings after one year with 5% interest
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

# Print the results
print("Your monthly savings are $", monthlySavings)
print("Projected savings after one year, with interest, is: $", projectedSavings)
