Name_List = []
count = int(input())  # Taking input number
dict_Name = {}

for i in range(count):
    name = input()
    marks = int(input())
    dict_Name[name] = marks

# for i in dict_Name:
#     if (dict_Name[i+1]>dict_Name[i]):

for key, value in sorted(dict_Name.items()):
    print(key,value)
