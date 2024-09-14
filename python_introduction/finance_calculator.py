monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthl_savings = monthly_income - monthly_expenses
Projected_Savings = monthl_savings * 12 + (monthl_savings * 12 * 0.05)
print("Your monthly savings are ",monthl_savings,".")
print("Projected savings after one year, with interest, is: $",Projected_Savings,".")
