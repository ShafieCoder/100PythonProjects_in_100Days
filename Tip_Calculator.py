## calculate the tip on the bill and then divide the bill among the people 

#Welcome to the Tip-Calculator app
print("Welcome to the tip calculator!") 

# get the bill, tip percentage and the number of people who share the food
bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))

# calculat the final payment and determine the share for each person
bill_with_tip = bill * (1+tip_percentage/100)
person_share = round(bill_with_tip / Number_of_people,2)

# print final result
print(f"Each person should pay: ${person_share}")
