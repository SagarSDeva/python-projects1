#BMI calculator 2.0
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight/height**2)
if(BMI<18.5):
    print(f"your BMI is {BMI} you are Underweight Eat more")
elif(BMI>18.5):
    if(BMI<25):
        print(f"your BMI is {BMI} you have Normal weight")
    elif(BMI>25):
        if(BMI<30):
            print(f"your BMI is {BMI} you  have overweight")
    elif(BMI>30):
        if(BMI<35):
            print(f"your BMI is {BMI}you have a Obese")
    elif(BMI>35):
        print(f"your BMI is {BMI} are clinically obese")