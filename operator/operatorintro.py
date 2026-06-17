"""
        Operators:
            # Operators is a symbol that performs certain operations between operands.
            we use operator to do logical and mathmatic equation
            for example:
            c = a + b

            #Here,
            =,+  are operators.
            a,b,c are operands.

            #Types of Operatiors:
            1. Arithmetic Operators: 
                    a. + (addition operator)
                    b. - (subtraction operator)
                    c. * (multiplication operator)
                    d. / (division operatior)
                    e. % (modulus operator)
                    f. ** (power operator or exponential operatior)
                    g. // (floor division operatior)


"""
# a. + (addition operator)it adds the two or more than two operand 
# example
a=5
b=6
sum=a+b#here a and b are operand and (+) symbole is operator#concation property
print(sum)
# output:11
a="ram"
b="shyam"
sum=a+b#concation property
print(sum)
# output:ramshyam
#   b. - (subtraction operator)it subtract two or more than two operand
a=5
b=6
sub=b-a
sub_1=a-b
print(sub)
print(sub_1)
# output1
# output-1
#  c. * (multiplication operator)it multiply two or more than two operand
a=5
a=5
b=6
sub=b*a
sub_1=a*b
print(sub)
print(sub_1)
# output:30
# output:30
#  d. / (division operatior)it divide two operand
a=5
num_1=30
num_3=90
num=num_1/num_3
print(num)
output:0.3333333333333333
# e. % (modulus operator)it gives remainder of two operand after division
num_1=90
num_3=30
mod=num_1%num_3
print(mod)
# output:0
#  f. ** (power operator or exponential operatior)it calculate the power of intizer value
a=2
b=3
c=a**b
print(c)
# output:8
# g. // (floor division operatior)it only gives the whole number and ignore the decimal value
a=3.14
b=1.5
c=a//b
print(c)
# output:2.0
# if the radius of circle is 15 meter find its are(formula=pie*r^2)
# wap to take a length and width from user and find the area and peremeter of rectangle 
# output:the area of rectangle is :value
# output :The peremeter of rectangle is:value
radius=15
pie= 3.14159
formula=pie*radius**2
print(formula)
# output:706.85775
length=float(input("enter length : "))
width=float(input("enter length : "))
area=length*width
perimeter=2*(length*width)
print("the area of rectangle is ",area)
print("the peremeter of rectangle is ",perimeter)