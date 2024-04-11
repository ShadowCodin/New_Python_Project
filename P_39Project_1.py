import random
Rock = 1
Paper = 2
Scissors = 3
Users_choice = int(input("Enter: \n1-(For Rock) \n2-(For Paper) \n3-(For Scissors) \n:- "))
Computers_choice = random.randint(1, 3)
if Users_choice == Computers_choice:
    print("Its a Draw..")
elif Users_choice == 1 and Computers_choice == 2:
    print("You Lose!")
elif Users_choice == 1 and Computers_choice == 3:
    print("You Win!")
elif Users_choice == 2 and Computers_choice == 1:
    print("You Win!")
elif Users_choice == 2 and Computers_choice == 3:
    print("You Lose!")
elif Users_choice == 3 and Computers_choice == 1:
    print("You Lose!")
elif Users_choice == 3 and Computers_choice == 2:
    print("You Win!")
else:
    print("wrong input.")
