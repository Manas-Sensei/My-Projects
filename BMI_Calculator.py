height = input("What is your height(in meters)?")
weight = input("What is your weight(in Kilos)?")
weight_as_int = int(weight)
height_as_int = float(height)
bmi = weight_as_int / height_as_int ** 2
bmi_as_int = int(bmi)
if bmi_as_int <= 18.5 :
    print(f"your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi_as_int <= 25:
    print(f"your BMI is {bmi}, you are perfectly healthy.")
elif 25 < bmi_as_int < 30 :
    print(f"your BMI is {bmi}, you are overweight.")
else:
    print(f"your BMI is {bmi}, you are obese.")