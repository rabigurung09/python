"""
1. Write a function to find the cube of a number.
2. Write a function to check whether a number is even or odd.
3. Write a function to find the largest of two numbers.
4. Write a function to deposit money into a bank account.
5. Write a function to withdrawn money into a bank account.   
6. if the per unit price of electricity bill is 12 then calculate the total price of 56 unit.
7. Write a Python program using three user-defined functions to:
    Deposit money
    Withdraw money
    Display the current balance
    
    """
    
# 1. Write a function to find the cube of a number.
def cube(n):
    return n ** 3
print(cube(int(input("enter your number: "))))


# 2. Write a function to check whether a number is even or odd.
def check(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
check(int(input("enter your num:")))




def check_num(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(check_num(int(input("enter your num: "))))




# 3. Write a function to find the largest of two numbers.
def find_lar(num,num_1):
    if num > num_1:
        return "num is largest among two number "
    else:
        return "num_1 is largest among two number"
print(find_lar(int(input("enter your num: ")),int(input("enter your num_1: "))))



# 4. Write a function to deposit money into a bank account.
balance = 0
def bank(balance,deposite):
    balance += deposite
bank(0,int(input("enter your cash: ")))


# 5. Write a function to withdrawn money into a bank account.
def bank(current_amount,withdrw_amount):
    current_amount  -= withdrw_amount
    return current_amount
current_amount = 1000
current_amount= bank(1000,int(input("enter your withdraw amount: ")))
print(current_amount)





# 6. if the per unit price of electricity bill is 12 then calculate the total price of 56 unit.
def bill(a,b):
    a *= b
    return a
a =12
a =bill(12, int(input("enter your unit: ")))
print(a)

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



