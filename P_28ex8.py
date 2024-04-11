""""
Year = int(input("Enter the year: "))
if(Year%4==0):
    if(Year%100==0):
        if(Year%400==0):
            print('"It\'s a Leap Year".')
        else:
            print('"It\'s not a Leap Year".')
    else:
        print('"It\'s a Leap Year".')
else:
    print('"It\'s not a Leap Year".')
"""