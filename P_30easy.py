Size = input("Which Pizza size do you want (S/M/L)? ")
Bill=0
if Size=="S" or Size=="s":
    Bill+=100
elif Size=="M" or Size=="m":
    Bill+=200
elif Size=="L" or Size=="l":
    Bill+=300
else:
    exit("Wrong input! \nPls try again ")

Pepperoni = input("Do want pepperoni on your pizza (Y/N)")
if Pepperoni=="Y" or Pepperoni=="y":
    if Size == "S" or Size == "s":
        Bill+=30
    elif Size == "M" or Size == "m":
        Bill += 50
    elif Size == "L" or Size == "l":
        Bill += 50
    else:
        print()
elif Pepperoni=="n" or Pepperoni=="N":
    print()
else:
    print()
Cheese = input("Do you want extra cheese? (Y/N)")
if Cheese=="Y" or Cheese=="y":
   Bill+=20
else:
    print()
print(f"Your total would be {Bill}Rs. \n Thanks for ordering from us!...")