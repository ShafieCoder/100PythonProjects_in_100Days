# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_float = float(weight)
height_float = float(height)
BMI  = round(weight_float/height_float**2,1)
print(f"Your BMI is: {round(BMI,1)} ")

# Determine the comndition of bmi (Day3-project)

if bmi< 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")

elif bmi <= 25:
  print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi<= 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi <= 35:
  print(f"Your BMI is {bmi}, you are obese.")

else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
