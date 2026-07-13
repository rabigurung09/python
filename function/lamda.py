"""=====lamda function ====
# a lamda function is small ,anonymous function that does not have name 

# we use "lamda" keyword to define lamda function.

# syntax
lamda parameter :expression


here,
parameter ==> one or more
but,
expression ==> only one 
this expression is execute (runs) and return result


"""
# explain 
result = lambda a,b,c:a+b+c
print(result(2,4))
# output=6

# area of rect
output = lambda l,b:l*b
print("the area of rectangle is : ",output(3,7))
# output=the area of rectangle is :  21

# area of square:
output_1 =lambda a:a**2
print("the area of square :",output_1(12))
# output:the area of rectangle is :  21