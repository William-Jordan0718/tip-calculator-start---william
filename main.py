#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What was your bill?\n"))

tip = int(input("What percent would you like to tip? 10, 12, 15?\n"))

split = int(input("How many people will split the Bill?\n"))

tip_amount = tip/100

pay = (bill + (bill * tip_amount))/split

final = round(pay, 2)

print(f"You will have to pay ${final}")