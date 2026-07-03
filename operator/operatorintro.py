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
"""
        Operators:
            # Operators is a symbol that performs certain operations between operands.
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

                    
            2. comparasion operator(Relational operatior):
                    #Used to compare two values.
                    #Return True or False.
                a. == (equal to operator)
                b. != (not equal to )
                c. >  (greater than)
                d. >= (greater than or equal to)
                e. < (less than)
                f. <= (less than or equal to)

                

        3. Assignment Operator:
                a. = (assignment operatior)
                b. +=(addition assignment operator)
                c. -=
                d. *=
                e. /=
                f. %=
                g. **=
                h. //=


        4. Logical Operatior:
                a. or
                b. and 
                c. not


        5. Membership Operator:
                #membership operator is used to check value exists(present) in the sequence(eg:string,list,tuple,etc.) or not.
                #Returns True if value exist(present) otherwise return False.
                a. in
                b. not in
        
                
        6. Identity Operator:
                #Checks the memory location of two objects(variable).
                #Return True or False.

                a. is:
                        #Returns True if both object(variable) have same memory location, otherwise return False.

                b. is not:
                        #Return True if both object(variable) have not same memory location, otherwise return False.

                        

        7. Bitwise operator:            works on bit.
                a. | (Bitwise or operator)
                b. & (Bitwise and operator)
                c. ~ (Bitwise not operator)    #Shitt + TapKoMathikoButton
"""

#1. Arithmetic Operator: [+, -, *, /, %, **, //]
# a = 5
# b = 2

# print(a+b)        #7
# print(5+2)

# print(a-b)          #3
# print(a*b)          #10
# print(a/b)          #2.5
# print(a%b)            #1                   #gives remainder
# print(11%3)         #2

# print(a**b)           #25
# print(2**5)             #32

# print(a//b)             #2




#2. Comparison Operator(Relational Operator):  [==, !=, >, >=, <, <=]
#Return True or False

# a = 5
# b = 2

# print(a == b)  #False
# print(a != b)    #True
# print(a>b)      #True
# print(a>=b)     #True
# print(a<b)          #False
# print(a<=b)         #False


#3. Assignment opertors: [=, +=, -=, *=, /=, %=, **=, //=]
# a = 5
# b = 2

# a+=b            #a = a+b
# a-=b             #a = a-b
# a+=5            #a = a+5 
# a*=b            #a = a*b
# a/=b            #a = a/b
# a**=b           # a = a**b   
# a%=b               # a = a%b   

# a//=b             #a = a//b              

# print(a)






#4. Logical operatiors: or, and, not
 #Works on boolean values.[i.e. Return True or False]


# print(True or True)             #True

# print(5>2 or 3<1)                # print(True or False)            #True

# print(True or False)            #True
# print(False or False)           #False
# print(False or True)               #True

# print(True and True)            #True
# print(True and False)           #False


# print(5>2 and 3<1)              #print(True and False)  #False




#5. Membership Operators:  

# print("d" in "deepak")        #True
# print("dp" in "deepak")         #False
# print("wx" in "deepak")         #False


# print("d" not in "deepak")        #False
# print("dp" not in "deepak")        #True
# print("wx" not in "deepak")         #True


# name = "deepak"

# print("d" in name)              #True



#6. Identity Operators: is, is not

# a =[1,2,3]
# b= [10,20,30]

# c = [1,2,3]

# d = a

# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))


# print(a == c)         #True             #== operator checks value
# print(a is c)           #False

# print(a is d)         #True

# print(b is c)           #False
# print(c is d)           #False


# print(a is not c)       #True
# print(c is not d)       #True

# print(a is not d)       #False




# x = 10
# y = 20
# z = 10

# print(id(x))
# print(id(y))
# print(id(z))


# print(x == z)   #True           #value check
# print(x is z)   #True           #memory location check




#7. Bitwise Operators: |, & , ~

a = 5
b = 2

# print(a|b)              #7
# print(a&b)              #0

# print(~a)               #~5         #add 1 and add -ve sign          #-6


print(~(a|b))           #~7                     #add 1 and add -ve sign #-8