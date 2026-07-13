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



# Question 1: Library Fine Calculator

# A library charges fines for overdue books.

# Write a Python function calculate_fine(days_late) that applies the following rules:
# First 5 days: Rs. 2 per day
# Next 5 days: Rs. 5 per day
# More than 10 days: Rs. 10 per day for the remaining days

# The function should return the total fine.

result = lambda day,rate:day * rate
print("fine is: ",result(2,5))


# factorial = n * factorial(n-1)

def fac(n):
    result=1
    for i in range (1 ,n+ 1):
        result *= i
    return result
print(fac(int(input("enter num: "))))


def factorial(n):
    return n*factorial (n-1)
