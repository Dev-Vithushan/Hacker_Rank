Name = "Vithshan"
Age = 23
University = "University of Jaffna"
Level = "2S"
Money = 20000000

# Printing on linear form
print("{} is a student of {} his age is {} and he is studying level on {}. He has {:,}".format(
    Name, University, Age, Level, Money))

print("{:,.2f}".format(Money))  #20,000.0000
