#MINI SHOPPING CLI PROGRAM 
import time
import random
print("WELCOME TO MY CART SHOP")
item = ["KITCHEN-SET","BLAZERS","WILD CRAFT SCHOOL BAGS","BEDSHEETS"] 
cost = ["Rs 3600","Rs 4000","Rs 1250","900"]
x = []
l = []
print()
for i,j in zip(item,cost):
    print(i,"=",j)
    print()
choice = 'y' or 'n'
count = 0
 
while choice == 'y' or choice == 'YES' or choice == 'yes' or choice =='Y':
    print()
    user_1 = input("Enter the name of the item which you would like to purchase : ")
    print()    
    user_2 = int(input("Enter the cost of the item which you would like to purchase : {} ".format("Rs")))
    print()
    if user_2 == 35600 or user_2 == 2000 or user_2 == 1200:
        l.append(user_2)
    else:
        print()
        print("WAIT........ SECONDS.")
        time.sleep(1)
        break
    if user_1 in item:
        x.append(user_1)
        print()
        print(user_1,"has been added to your cart.")
        print()
        count += 1
    else:
        print()
        print("Item not found.Try again.")
    choice = input("Do you want to add any other item to your cart : ")
 
while choice == 'n' or choice == 'no' or choice == 'NO' or choice == 'N':
    print()
    print("There are",count,"items in your cart")
    print()
    print("Total : {}".format("Rs"),sum(l))
    print()
    user_4 = input("Proceed to checkout (y/n) : ")
    if user_4 == 'n':
        print()
        print("ABORTING IN 5 SECONDS")
        time.sleep(5)
        break
    else:
        print()
        user_5 = input("Select payment method (Credit/Debit) : ")
        print()
        print("PROCESSING")
        r = 0
        while r <= 2:
            print(".")
            time.sleep(1)
            r += 1
        print()
        print("CAPTCHA GENERATION")
        b = 0
        while b <= 3:
            print(".")
            time.sleep(1)
            b += 1
        print()
        print("Enter the captcha given below.")
        print()
        captcha = random.randint(111111,999999)
        print(captcha)
        print()
        user_6 = input()
        if user_6 != captcha:
            "ABORTING IN 5 SECONDS."
        else:
            continue
        f = 0
        print()
        print("AWAITING IMFORMATION.")
        while f <= 5:
            print(".")
            time.sleep(1)
            f += 1
        print()
        print("TRANSACTION SUCCESSFUL.")
        print()
        print("**************************THANK YOU FOR CHOSING MY CART SHOP*****************************")
        time.sleep(15)
        break
