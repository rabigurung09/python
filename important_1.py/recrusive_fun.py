# def lif(n):
#     if n == 0:
#         print("you are in ground floor")
#         return
#     print("you are in ",n,"floor , your next floor is ",(n-1))
#     lif(n-1)
# lif(int(input("enter your num: ")))








# # write  a program to find the factorial of a number using recursive function.
# # n* factorial(n-1)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

 
# n = int(input("Enter a number: "))
# print(factorial(n))



# # WAp to find the sum of natural numbers

# # reverse the below given string:
# # string = "Kathmandu"

# def rev(n):
#     return n
# n=['kathamandu']
# n.__reversed__()
# print(n)

# def n (a):
#     return a
a = [1,5,4,9,8]
print(a)
a.sort(reverse=True)
print(a)



city = ["kathamandu"]
city.sort(reverse = True)
print(city)
def reverse_string(s):
    # Base case: if the string is empty, return it
    if len(s) == 0:
        return s
    # Recursive case: reverse the rest of the string and add the first character at the end
    return reverse_string(s[1:]) + s[0]

city = "Kathmandu"
reversed_city = reverse_string(city)
print(reversed_city)
# Reverse a string in Python
city = "Kathmandu"
reversed_city = city[::-1]
print(reversed_city)
