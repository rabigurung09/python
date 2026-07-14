"""
1. Write a function to find the cube of a number.
2. Write a function to check whether a number is even or odd.
3. Write a function to find the largest of two numbers.
4. Write a function to deposit money into a bank account.
5. Write a function to withdrawn money into a bank account.   
6. if the per unit price of electricity bill is 12 then calculate the total price of 56 unit.
7. Write a Python program using three user-defined functions to:
    Deposit money
    Withdraw money
    Display the current balance
    
    """
  
    
# 1. Write a function to find the cube of a number.  
def cube(n):
    print(n**3)
cube(int(input("enter your num: ")))


# 2. Write a function to check whether a number is even or odd.
def num(n):
    if n%2 == 0:
        print("num is even")
    else:
        print("num is odd")
num(int(input("enter your num: ")))



# 3. Write a function to find the largest of two numbers
def num(n,n_1):
    if n > n_1:
        print("n is largest")
    else:
        print("n_1 is largest")
num(int(input("enter your num")),int(input("enter your num")))




# 4. Write a function to deposit money into a bank account.
def bank(t_c,d_a):
    t_c += d_a
    return t_c
t_c =100000
t_c = bank(100000,(int(input("enter your depo amt: "))))
print(t_c)



# 5. Write a function to withdrawn money into a bank account. 
def bank(c_amt,w_amt):
    c_amt -= w_amt
    return c_amt
c_amt =100000
c_amt =bank(100000,(int(input("enter your w_amt: "))))
print(c_amt)


# 6. if the per unit price of electricity bill is 12 then calculate the total price of 56 unit.
def total(a,b):
    print(a * b)
total(12,56)


















