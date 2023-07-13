#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
tbill = int(input("What was the total bill:"))
tip = int(input("How much tip would you like to give in %:"))
people = int(input("How many people to split the bill:"))
per = tip / 100
final_tip = per * tbill
bill = (tbill / people) + final_tip / people
print(f"Each person should pay:{round(bill, 2)}")
