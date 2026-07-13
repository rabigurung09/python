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

# 7. Write a Python program using three user-defined functions to:
    # Deposit money
    # Withdraw money
    # Display the current balance
    
def depo(current_balance,depo_balance):
    current_balance += depo_balance
    return current_balance
current_balance = 0
current_balance = depo(0,int(input("enter your deposite amount: ")))
print(current_balance)
def with_draw(current_balance,with_dra):
    current_balance -= with_dra
    return current_balance
current_balance= with_draw(current_balance,int(input("enter your withdraw amount: ")))
print(current_balance)

