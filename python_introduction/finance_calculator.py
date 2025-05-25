#Prompt the user for their monthly income
monthlyIncome = int(input("Enter your monthly income: "))
#Ask for their total monthly expenses:
totalMonthlyExpense = int(input("Enter your total monthly expenses: "))
#Calculate the monthly savings
montlySavings = monthlyIncome - totalMonthlyExpense
#Project Annual Savings:
ProjectedAnnualSavings = ((montlySavings*12) * 5/100 *1) + (montlySavings*12)

print(f"Your monthly savings are {montlySavings} ")
print(f"Projected savings after one year, with interest, is: {ProjectedAnnualSavings}")