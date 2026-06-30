# """
# Write a program to check whether a number is positive or negative.
# Write a program to check whether a number is even or odd.
# Write a program to find the largest of two numbers  by taking number from user.
# Write a program to find the smallest of two numbers.
# Write a program to check whether a person is eligible to vote.
# Write a program to check whether a student has passed or failed (pass marks = 40).
# Write a program to compare two strings.
# Write a program to check whether a number is divisible by 5.
# Find the largest among three numbers.
# Find the smallest among three numbers.
# Check whether a number is divisible by both 3 and 5.

# """
# # Write a program to check whether a number is positive or negative.
# user=int(input("enter a number : "))
# if user<0:
#     print("number is negative")
# elif user>0:
#     print("number is positive")
# else:
#     print("number is zero")
# # output= 
# # enter a number : 3
# # number is positive
# # enter a number:0
# # number is zero
# # Write a program to check whether a number is even or odd.
# user_1=int(input("enter a number : "))
# if user_1%2==0:
#     print("your num is even")

# else:
#    print("number is odd")
# # output=
# # enter a number : 4
# # number is even
# # enter a number: 13
# # number is odd


# # Write a program to find the largest of two numbers  by taking number from user.
# user_1 = int(input("enter a number"))
# user_2 = int(input("enter a number"))
# if user_1>user_2:
#     print("user_1 is largest")
# else:
#     print("user_2 number is largest")
# # output=enter a number2
# # enter a number6
# # user_2 number is largest


# # Write a program to find the smallest of two numbers.
# user = int(input("enter a number user : "))
# user_1 = int(input("enter a number user_1 : "))
# if user<user_1:
#     print("user is smallest")
# else:
#     print("user_1 is smallest")
# # output=3


# # Write a program to check whether a person is eligible to vote.
# age_of_person=int(input("enter your age : "))
# if age_of_person>=18:
#     print("you are eligible")
# else:
#     print("you are not eligible")
# # output=enter your age : 19
# # you are eligible

# # Write a program to check whether a student has passed or failed (pass marks = 40).
# student=int(input("enter your marks : "))
# if student > 90:
#     print("you score a+")
# elif student > 80:
#     print("you score b+")
# elif student >= 40:
#     print("you have pass")
# else:
#     print("you have fail")
# # output=enter your marks : 40
# # you have pass


# # Write a program to compare two strings.
# inut=(input("enter a string : "))
# inut_2=(input("enter a string"))
# if inut==inut_2:
#     print("string are equal")
# else:
#     print("atring are not equal")
# # output=3


# # Write a program to check whether a number is divisible by 5.
# num=int(input("enter a number: "))
# if num%5==0:
#     print("number can be divisible by 5")
# else:
#     print("number is not divisible by 5")
# # output=enter a number: 50
# # number can be divisible by 5


# # Find the largest among three numbers.
# a=20
# b=30
# c=50
# if a>b and b>c:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# else:
#     print("c is largest")
# # output=
# # c is largest


# # Find the smallest among three numbers.
# a=34
# b=93
# d=90
# if a<b and a<d:
#     print("a is smallest")
# elif b<a and b<d:
#     print("b is smallest")
# else:
#     print("d is smallest")
# # output= a is smallest


# Check whether a number is divisible by both 3 and 5.
user=int(input("enter a num : "))
if user%3==0 and user%5==0:
    print("number is divisible by both 5 and 3")
else:
    print("number is not divisible by ")
# output:enter a num : 15
# number is divisible by both 5 and 3