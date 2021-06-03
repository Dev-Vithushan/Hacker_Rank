# # Reading the files

# file_name = 'text documents/details.txt'

# # Writting the files mentioning the w must
# with open(file_name,'w') as file_object_write:
#     file_object_write.writelines("I love Python\n")
#     file_object_write.writelines("I love Java1\n")
#     file_object_write.writelines("yes i am ready\n")
#     file_object_write.writelines("i am okay\n")
#     file_object_write.writelines("finished everything")

# #Appending the lines mentioning the 'a' must
# with open(file_name,'a') as file_object_add:
#     file_object_add.write("\nhello")
#     file_object_add.write("\ni am now did that part")


# #Reading the files
# with open(file_name) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.strip())  # ignoring the space

prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")


txt_file = "text documents/details.txt "
with open(txt_file) as obj:
    read_line  = obj.read(txt_file)
print(read_line.strip())