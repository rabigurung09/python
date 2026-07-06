# """1.Write a program to calculate grades based on marks.
# 90–100 : A
# 80–89  : B
# 70–79  : C
# 60–69  : D
# Below 60 : F

# 2. Write a program to display the day of the week based on a number (1–7).
# 3. Write a program to classify a person's age.
# 0–12 : Child
# 13–19 : Teenager
# 20–59 : Adult
# 60+ : Senior Citizen

# 4. Create a simple login system with three attempts.
# 5. Find the second largest of three numbers.
# 6. ATM withdrawal system.
# 7. Login system using username and password.
# 8. Restaurant bill with discount.
# 9.Movie ticket pricing based on age.
# 10. Restaurant bill with discount."""



# # 1.Write a program to calculate grades based on marks.
# # 90–100 : A
# # 80–89  : B
# # 70–79  : C
# # 60–69  : D
# # Below 60 : F


# user=int(input("enter yor marks"))
# if user >= 90:
#     print("a")
# elif user >= 80:
#     print("b")
# elif user >=70:
#     print("c")
# elif user >=60:
#     print("d")
# else:
#     print("f")    



# # 2. Write a program to display the day of the week based on a number (1–7).

# user_1=int(input("enter the number : "))
# if user_1 == 1:
#     print("sunday")
# elif user_1 ==2:
#     print("monday")
# elif user_1 == 3:
#     print("thusday")
# elif user_1 == 4:
#     print("wenesday")
# elif user_1 == 5:
#     print("thusday")
# elif user_1 == 6:
#     print("friday")
# elif user_1 == 7:
#     print("satarday")
# else:
#     print("invalid")
    
    

# # 3. Write a program to classify a person's age.
# # 0–12 : Child
# # 13–19 : Teenager
# # 20–59 : Adult
# # 60+ : Senior Citizen
# user_2=int(input("enter your age : "))
# if user_2 <= 0:
#     print("invalid")
    
# elif user_2 <= 12:
#     print("child")
# elif user_2 <=19:
#     print("teenager")
# elif user_2 <= 59:
#     print("adult")
# else:
#     print("senior citizen")


# # 4. Create a simple login system with three attempts.

# user_name="rabi"
# password="12@rabi"

# usr = input("enter your user name : ")
# pas = input("enter your passoword : ")

# if usr == user_name and pas == password:
#     print("login sucessfull")
# else: 
#     print("invalid password or user_name")
    
    
# # using while loop
# user_name= "rabi"
# password ="rabi@123"
 
 
# attemt = 1
# while attemt<= 3:
#     usr=input("enter your user_name: ")
#     pas=input("enter yor password")
#     if usr == user_name and pas == password:
#         print("login sucessfull")
#         break
#     elif usr != user_name and pas != password:
#         print("invalid password and user_name")
#         attemt += 1
#     if attemt>3:
#         print("invalid")   
        
        
        
# ==== using for loop====
# user_name="admin"
# password="rabi@123"
# attemt=1
# user_1=input("enter yor user_name: ")
# user_2=input("enter your password")
# for i in user_1 :
#     if i == user_name:
#         print("user name correct")
#     elif i != user_name :
#         print("user name not correct")
# for t in user_2 :
#     if t == password:
#         print("password correct")
#     elif t != password:
#         print("password incorrect")
#     if i == user_name and t == password:
#         print("log in sucessfull")
#         break
#     elif i != user_name and t != password:
#         print("login unsucessfull")
#         attemt +=1
#         if attemt >3:
#             print("invalid account is locked now")
        # unexpected
user_name="admin"
password="rabu@133"
for attempt in range(1,4):
    user=input("enter your user name: ")
    pas=input("enter your password: ")
    if user == user_name and pas ==password:
        print("login sucessfull")
        break
    else:
        print("login unsucessful")
        if attempt==3:
            print("account locked")
            
            
            
# ===another=====
user_name="admin"
password="rabu@133"
for attempt in range(1,4):
    user=input("enter your user name: ")
    pas=input("enter your password: ")
    if user == user_name and pas ==password:
        print("login sucessfull")
        break
    else:
        print("invalid user_name or password")
        print("attemt left", 3 - attempt)
    if attempt == 3:
        print("incorrect user_name or  password")
        print("account_locked")
    
       
  

        
  


        
        
# 5. Find the second largest of three numbers.
# user_1=int(input("enter your number: "))
# user_2=int(input("enter your number: "))
# user_3=int(input("enter your number: "))
# if user_1 > user_2 and user_3:



    
    
    
    
    
    