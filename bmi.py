weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
else:
    category = "Overweight"

print("\nWeight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))