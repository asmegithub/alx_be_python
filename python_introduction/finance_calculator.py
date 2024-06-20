monthlyIncome=int(input("Enter your monthly income: "))
monthlyExpense=int(input("Enter your total monthly expenses: "))
monthlySaving=monthlyIncome-monthlyExpense
projectedSavings = monthlySaving * 12 + (monthlySaving* 12 * 0.05)
print("Your monthly savings are $",monthlySaving)
print("Projected savings after one year, with interest, is: $",projectedSavings)