print ("Welcome to the tip calculator.")
bill = input ("What is the total bill?$")
tip = input ("What percentage tip would you like to give? 10, 12, or 15?")
number = input ("How many people will split the bill?")

#Convert into correct format
bill = float(bill)
tip = float(tip)/100
number = int(number)

#Calculate
total =(bill) + (bill * tip)
per_person = total / number
final = round(per_person, 2)

print(f"Each person should pay: ${final:.2f} ")
