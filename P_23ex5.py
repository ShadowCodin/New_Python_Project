Age = (input("What is your age in days"))
Age_Days = 32850-int(Age)
Age_Months = int(Age_Days)/30
print(f"You will live {32850-int(Age)} days more.")
print(f"You will live {int(Age_Days)//30} months and {int(Age_Days)%30} days more.")
print(f"You will live {int(Age_Months)//12} years and {int(Age_Months)%12} months more.")
