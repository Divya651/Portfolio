loan_principle = int(input("Please enter the loan principle: "))
loan_term = int(input("Please enter the loan term in months: "))
interest_rate = float(input("Please enter the annual interest rate of the loan in decimal: "))

loan_amount = (float(loan_principle * (1 + interest_rate / 12)**loan_term))-loan_principle

print("The amount of interest in this loan is $", loan_amount )