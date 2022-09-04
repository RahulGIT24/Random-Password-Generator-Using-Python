import random
import datetime
# * Project: password Generator
# * Made By Rahul
# * Location Ghar pe
# * Date - 20-03-2022
x = datetime.datetime.now()
while(True):
    print("\tPress q to quit")
    o = input("For which site you want to generate password: ")
    if (o == 'q'):
        break
    n = input("Type g to generate password\n")
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOP"
    numbers = "1234567890"
    symbols = "!@#$%^&*{}[]?/<>,.;:"

    all = lowercase+uppercase+numbers+symbols
    length = 16
    password = "".join(random.sample(all, length))
    if(n == 'g'):
        print(f"password for {o} is {password}")
    else:
        print("Invalid command")

    with open("password.txt", 'r') as f:
        f.read()
    with open("password.txt", 'a') as f:
        f.writelines(f"\nPassword generated for {o} on {x} is :  {password}")
    f = open("password.txt", 'a')
    f.close()
