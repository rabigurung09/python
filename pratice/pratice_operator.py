""".
Take the radius of a circle and find its area.
Take marks of 5 subjects and find the total and average.
Take the principal, rate, and time from the user and calculate simple interest."""
user=int(input("enter 1 subject marks : "))
user_1=int(input("enter 2 subject marks : "))
user_2=int(input("enter 3 subject marks : "))
user_3=int(input("enter 4 subject marks : "))
user_4=int(input("enter 5 subject marks : "))
total=user+user_1+user_2+user_3+user_4
print("your total marks : ",total)
average=total/5
print("your average marks is : ",average)
user=int(input("enter principal : "))
user_1=int(input("enter rate : "))
user_2=int(input("enter time : "))
si=user*user_1*user_2/100
print("simple intrest is : ",si)