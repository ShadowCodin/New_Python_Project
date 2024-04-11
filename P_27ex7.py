"""""
Weight = input("What is your weight in KGs")
Height = input("What is your height in meters")
BMI = float(Weight) / float(Height)**2
print("Your BMI is" + " " + str(int(BMI)))
if(BMI<=18.4):
    print("You are underweight. Gain some weight buddy!")
elif(18.4<BMI<=24.9):
    print("You are fit and fine.Nice work")
else:
    print("You are overweight. You need to lose weight, go to gym daily")
print("We hope you got your correct BMI")
"""