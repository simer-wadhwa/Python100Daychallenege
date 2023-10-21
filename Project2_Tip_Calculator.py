print("Welcome to the tip Calculator. ")
amount = float(input(" what was the total bill ? $ "))
tip = int(input(" what percentage tip would you like yo give ? 10 ,12 or 15? "))
people = int(input(" How many people to split the bill? "))
# tip = tip / 100
# temp = amount * tip
amount = ((tip/100*amount) + amount)/people
#bill = amount/people
#bill = round(bill,2)
amount = "{:.2f}".format(amount)
print("Each person should pay: ", amount)


