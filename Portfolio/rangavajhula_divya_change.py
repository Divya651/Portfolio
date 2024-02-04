number_cents = int(input("Please enter a number of cents: "))
quarters = number_cents // 25
dimes = number_cents % 25 // 10
nickels = number_cents % 25 % 10 // 5
pennies = number_cents % 25 % 10 % 5 // 1

print("Coins: ", quarters, "quarters, ", dimes, "dimes, ", nickels, "nickels, ", pennies, "pennies")