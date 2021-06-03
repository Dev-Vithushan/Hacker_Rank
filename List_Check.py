def isUnique(tested_list):                              #Testing the uniquness of list
    if len(tested_list) == len(set(tested_list)):
        print("Uniquness")
    else:
        print("no uniquness found")


My_List1 = [1, 3, 4, 2, 4, 2, 3, 4, 2, 4]  # Creating a list

# Filltering a list using linear function
My_List2 = [number for number in My_List1 if number > 3]

My_List3 = [i ** 2 for i in My_List1]  # Filtering list linear function

My_List4 = list(zip(My_List1, My_List3))  # Covering the items

My_List5 = [1, 2, 3, 4, 5]

reversed_List = My_List5[::-1]              #Changing the order reversed

Nested_List = [[1,2],[3,4],[5,6]]           
flat_list = [i for j in Nested_List for i in j]

flat_list = [1,2,3,4,5,6,6,]
print(flat_list)

isUnique(My_List2)