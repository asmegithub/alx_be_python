
monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpense = int(input("Enter your total monthly expenses: "))

monthlySavings = monthlyIncome - monthlyExpense

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

# Print the results
print("Your monthly savings are $", monthlySavings)
print("Projected savings after one year, with interest, is: $", projectedSavings)
