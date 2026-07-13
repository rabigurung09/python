# """#1. Bank Withdrawal Create a function withdraw(balance, amount) that allows withdrawal only if the balance is sufficient.1
# #2. Shopping Discount (Lambda) Use a lambda function to apply a 15% discount if the purchase amount is Rs. 1000 or more.

# 3. Employee Salary
# Write a function salary(basic) that calculates:
# HRA = 20% of basic
# DA = 10% of basic
# Return the total salary.


# # # 5.Electricity Bill

# # # Write a function bill(units):
# # # First 100 units → Rs. 5/unit
# # # Next 100 units → Rs. 8/unit
# # # Above 200 units → Rs. 10/unit
# # # """

# # 1. Bank Withdrawal Create a function withdraw(balance, amount) that allows withdrawal only if the balance is sufficient.1
# def with_draw(balance,amount):
#     balance -= amount
#     return balance
# balance = 10000
# balance= with_draw(10000,int(input("enter your amount: ")))
# print(with_draw,balance)


# def with_draw(a,b):
#     return lambda amount:amount - balance
# print(with_draw,(100,99))


# def with_draw(balance,amount):
#     if balance > 1:
#         print(with_draw,balance-amount)
#     else:
#         print("balance not sufficent")
# with_draw(int(input("enter your balance")),int(input("enter your with_draw amount")))



# # #2. Shopping Discount (Lambda) Use a lambda function to apply a 15% discount if the purchase amount is Rs. 1000 or more.
# result = lambda amount: amount/100*15-amount if amount >= 1000 else amount
# print(result(int(input("enter your amount"))))


# # 3. Employee Salary
# # Write a function salary(basic) that calculates:
# # HRA = 20% of basic
# # DA = 10% of basic
# # Return the total salary.
# def salary (cash):
#     print(cash /100 *30 + cash)
# salary(int(input("enter your salary: ")))


# # 5.Electricity Bill

# # Write a function bill(units):
# # First 100 units → Rs. 5/unit
# # Next 100 units → Rs. 8/unit
# # Above 200 units → Rs. 10/unit
# # """
def elec(unit):
    if unit<= 100:
        print(unit*5)
    elif unit <=200:
        print(unit*8)
    else:
        print(unit*10)
user=int(input("enter your unit: "))
elec(user)