# Prompt user for monthly income and expenses
income = float(input("Enter your monthly income: ")
expenses = float(input("Enter your total monthly expenses: ")
# Calculate monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)
# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
# Output results
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
