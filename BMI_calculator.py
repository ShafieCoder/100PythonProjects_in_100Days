# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_float = float(weight)
height_float = float(height)
BMI  = weight_float/height_float**2
print(f"Your BMI is: {round(BMI,3)} ")