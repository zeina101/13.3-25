height = float(input("Enter your height in cm."))
weight = float(input("Enter your height in kg."))

BMI = weight/(height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight. Try to eat a bit more.")

elif BMI =24.9:
    print("Great! You're healthy.")

elif BMI <= 29.9:
    print("You're a but over your height's standard. Try eating a little less.")

elif BMI <= 34.9:
    print("You're severely overweight. You've got to eat lesser.")

elif BMI <= 39.9:
    print("YYou're obese, and you need to urgently do something about it.")

else:
    print("You are severely obese!!")    