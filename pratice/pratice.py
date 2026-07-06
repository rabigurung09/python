# 10. Restaurant bill with discount.
user=int(input("enter your bill: "))
if user < 5000:
    print(user)
if user >= 5000:
    i = user/100*20
    j = user - i
    print(j)
    


# 9.Movie ticket pricing based on age.
ticket_price = 300
user_1 = int (input("enter your age: "))
if user_1 <= 16:
    k=ticket_price/100*20
    o=ticket_price-k
    print("you are child and your movie ticket price is ",o)
else:
    print("300")
    
    
# ATM withdrawal system
total_balance= 40000
user_withdraw=int(input("enter your withdraw amount: "))
if user_withdraw <= total_balance:
    print("your with drawamount: " ,user_withdraw)
else :
    print("your account has insuffence balance")
    
    
# 5. Find the second largest of three numbers.
a = int(input("enter yor num: "))
b = int(input("enter yor num: "))
c = int(input("enter yor num: "))
if (a>b and a<c ) and (a>c and a<c):
    print("second largest num:",a)
elif (b>a and b<c) or (b>c and b<a):
    print("second largest num: ",b)
elif (c>a and c <b) or (c>b and c<a):
    print("second largest num: ",c)