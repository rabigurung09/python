user_1=int(input("enter your first num : "))
user_2=int(input("enter your second num : "))
operator=input("enter your operator : ")
if operator == "*":
    print(user_1*user_2)
elif operator == "+":
    print(user_1+user_2)

elif operator =="/":
    if user_2 != 0:
        print(user_1/user_2)
    else:
        print("envalid")
    

else:
    print(user_1-user_2)
