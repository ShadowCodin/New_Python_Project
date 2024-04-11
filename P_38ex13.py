List_1 = [1, 1, 1]
List_2 = [1, 1, 1]
List_3 = [1, 1, 1]
Final_List = [List_1,List_2,List_3]
#print(Final_List)
print(f"{List_1} \n{List_2} \n{List_3}")
position = input("Enter the position you wanna hide your essentials: ")
x = int(position[0])
y = int(position[1])
List_no = Final_List[x-1]
List_no[y-1] = 'X'
print(f"{List_1} \n{List_2} \n{List_3}")

