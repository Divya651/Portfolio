hourly_wage = int(input("Please enter your hourly wage: "))

hours_worked = int(input("Please enter the number of hours worked per week: "))

weeks_worked = int(input("Please enter the number of weeks worked this year: "))

Salary = (hours_worked * weeks_worked) * hourly_wage

print("Your salary so far this year is $", Salary)