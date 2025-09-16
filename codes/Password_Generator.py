import random
import string

print("This program generates a password of the users choice\n")
Pass_Length = int(input("How many characters would you like the password to be? \n"))

print("What additional features would you like?\n")
Pass_Letter = input("Password contais letters? (y/n) \n") == 'y'
Pass_Number = input("Password contains numbers? (y/n) \n") == 'y'
Pass_Symbol = input("password contains symbols? (y/n) \n") == 'y'


Pass_List = []
for i in range (Pass_Length):
    Pass_List.append(random.choice(Pass_Letter*(string.ascii_letters) + Pass_Number*(string.digits) + Pass_Symbol*(string.punctuation)))

Password_Final = ''.join(Pass_List)

print(Password_Final)
