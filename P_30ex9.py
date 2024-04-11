S = 100
M = 200
L = 300
P = 30
R = 50
C = 20
Order = input('Order your pizza please \n (Small/Medium/Large).')
if Order == "Small":
    print(f"You need to pay {S}Rs only.")
elif Order == "Medium":
    print(f"You need to pay {M}Rs only.")
elif Order == "Large":
    print(f"You need to pay {L}Rs only.")
else:
    print("Wrong input \n Please try again.")
Toppings = input('Do you want any toppings?')
if Order=="Small":
    if Toppings=="yes" or Toppings=="Yes":
        print(f"Your new total is {S+P}Rs")
    elif Toppings=="no" or Toppings=="No":
        print(f"Your total is {S}Rs only")
    else:
        print()
elif Order=="Medium":
    if Toppings=="yes" or Toppings=="Yes":
        print(f"Your new total is {M + R}Rs")
    elif Toppings == "no" or Toppings == "No":
        print(f"Your total is {M}Rs only")
    else:
        print()
elif Order=="Large":
    if Toppings=="yes" or Toppings=="Yes":
        print(f"Your new total is {L + R}Rs")
    elif Toppings == "no" or Toppings == "No":
        print(f"Your total is {L}Rs only")
    else:
        print()
else:
    print()
Cheese = input("Do you want extra cheese?")

if Toppings=="yes" or Toppings=="Yes":

    if Order=="Small":
       if (Cheese=="yes" or Cheese=="Yes"):
          print(f"Your new total is {S+C+P}Rs")
       elif Cheese=="no" or Cheese=="No":
          print(f"Your total is {S+P}Rs only")
       else:
          print()
    elif Order=="Medium":
       if Cheese=="yes" or Cheese=="Yes":
          print(f"Your new total is {M + C+R}Rs")
       elif Cheese == "no" or Cheese == "No":
          print(f"Your total is {M+R}Rs only")
       else:
          print()
    elif Order=="Large":
       if Cheese=="yes" or Cheese=="Yes":
          print(f"Your new total is {L + C+R}Rs")
       elif Cheese == "no" or Cheese == "No":
          print(f"Your total is {L+R}Rs only")
       else:
          print()
else:
    print()

if Toppings=="no" or Toppings=="No":
    if Order=="Small":
       if (Cheese=="yes" or Cheese=="Yes"):
         print(f"Your new total is {S+C}Rs")
       elif Cheese=="no" or Cheese=="No":
         print(f"Your total is {S}Rs only")
       else:
         print()
    elif Order=="Medium":
       if Cheese=="yes" or Cheese=="Yes":
         print(f"Your new total is {M + C}Rs")
       elif Cheese == "no" or Cheese == "No":
         print(f"Your total is {M}Rs only")
       else:
         print()
    elif Order=="Large":
       if Cheese=="yes" or Cheese=="Yes":
         print(f"Your new total is {L + C}Rs")
       elif Cheese == "no" or Cheese == "No":
         print(f"Your total is {L}Rs only")
       else:
         print()
else:
    print()
print("Thanks for coming!...")



