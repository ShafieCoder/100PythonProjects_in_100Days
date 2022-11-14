
import random
# set a random seed that make the results reproducible
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# It seprate names and put them in a list that seperated by a comma and a space
names = names_string.split(", ")


# find the number of people that share the bill and pick the name should pay for others
number_of_people = len(names)
random_choice = random.randint(0,number_of_people -1)
payer = names[random_choice]

# we can replace all of these last three lines with function choice()
# person_who_will_pay = random.choice(names)
print(payer + " is going to buy the meal today!")
# Sara, Sina, Soheil, Saba, Sohrab
