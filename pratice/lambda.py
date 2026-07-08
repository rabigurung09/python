"""Question 1: Library Fine Calculator

A library charges fines for overdue books.

Write a Python function calculate_fine(days_late) that applies the following rules:
First 5 days: Rs. 2 per day
Next 5 days: Rs. 5 per day
More than 10 days: Rs. 10 per day for the remaining days

The function should return the total fine.

Question 2: Age Eligibility Checker Using Lambda function.

A company wants to check whether a candidate is eligible to apply for a job.

Write a lambda function that accepts a candidate's age and returns:

"Eligible" if the age is 18 or above.
"Not Eligible" otherwise.

Example
Input:
Age = 20

Output:
Eligible"""
""""Question 1: Library Fine Calculator

A library charges fines for overdue books.

Write a Python function calculate_fine(days_late) that applies the following rules:
First 5 days: Rs. 2 per day
Next 5 days: Rs. 5 per day
More than 10 days: Rs. 10 per day for the remaining days

The function should return the total fine."""

def calculation(day):
    fine = 0
    if day <=5:
        fine = day*2
        
    elif day <=  10:
        fine = (5*2) + (day -5)*5
        
    else:
        fine = (35)+(day-10)*10
    return fine
user = int(input("enter your leave days:"))
print("your leave days is ",user,"and ur fine is", calculation(user))




"""Question 2: Age Eligibility Checker Using Lambda function.

A company wants to check whether a candidate is eligible to apply for a job.

Write a lambda function that accepts a candidate's age and returns:

"Eligible" if the age is 18 or above.
"Not Eligible" otherwise."""


b=18
lavel = lambda a  : a >= b
print("you are eligible")
print(lavel,(input("enter your age: ")))

age =lambda a  : a<b
print("you are not eligible")

user=int(input("enter your age: "))
print(user,lavel,age)


check_eli= lambda age: "you are eligible" if age>=18 else "you are not eligible"
user=int(input("enter your age: "))
print(check_eli(user))
