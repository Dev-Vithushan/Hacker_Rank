import time
My_Dictionary1 = {
    'Allamnq': 23,
    'Ashokkira': 23,
    'Davidoman': 24,
    'Moriskan': 23
}

My_Dictionary2 = {
    'Allam': 33,
    'Ashok': 13,
    'David': 14,
    'Moris': 33
}

My_Dictionary1["vithushan"] = 23
My_Dictionary2['Mathushan'] = 21

# Adding all dictionary key and value
My_Dictionary3 = {**My_Dictionary1, **My_Dictionary2}
# Adding key value for all dictionary
My_Dictionary3 = {*My_Dictionary1, *My_Dictionary2}

# Combining the two dictionary after 3.9
My_Dictionary4 = My_Dictionary1 | My_Dictionary2

print('Allam' in My_Dictionary1)  # Checking the value is or not(key)
print('Moris' in My_Dictionary4)

My_Dictionary1.pop('Moriskan')  # Removing from dictionary


My_Dictionary5 = {i: i**i for i in range(200)}  # creating the comprehensions


My_Dictionary6 = {
    'Apple' : 2300,
    'Dell' : 3400,
    'Intel' : 3555
}

My_Dictionary7 = {key:Value for (key,Value) in My_Dictionary6.items() if Value>3000}    #Filltering dictionary





