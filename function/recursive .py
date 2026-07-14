""" 
    4. Recursive Function(Recursion):
        #When a function call itself again and agian is known as recursive function.


        #syntax:

        #Function Defintion
        def functionName():
            #block of code 
            functionName()          #function that call itself(ie. Recursion)
        
            

        #Function Calling
        functionName()
"""
def stair(n):
    if n == 0:
        print("You reached the ground ")
        return
    print("to reach the stair",n, "we must  take stair",(n-1))
    stair(n-1)

stair(5)


# write  a program to find the factorial of a number using recursive function.
# n* factorial(n-1)
def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)
user = int(input("Enter a number: "))
print("the factorial of",user, "is: ", factorial(user))




# WAp to find the sum of natural numbers

# reverse the below given string:
# string = "Kathmandu"