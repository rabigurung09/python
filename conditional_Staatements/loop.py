# """ looping statement [iteration statement]
#     looping statement is used to repate (execute) block of code again and again until the condition become fale 
#     there is two type of loop:
#     a. for loop
#     for loop is used to repate a code for fix number if time
#     # syntax:
#     for value in iteratble (sequence):
#     # body (i.e body will executed until the condition become false)
#     b. while loop 
#     while loop is """
#     # ======range-====
#     # syntax :
#     # for value in iterable (start_value,end_value,increment_value)

# for i in range(1,10):
#     print(i)
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9

# # =====string===
# for i in "ram":
#     print(i)
# # r
# # a
# # m
# name="ram"
# for x in name:
#     print(x)
# # r
# # a
# # m
# list=["red","yellow","pink"]
# for i in list:
#     list=="yellow"
#     break
# print(i)

# tuple=("apple","orange","mango", "banana", "jackfruit","Litchi")
# for i in tuple:
#     if i == "orange":
#         continue
#     print(i)

tuple=("apple","orange","mango", "banana", "jackfruit","Litchi")
for i in tuple:
    if i == "Litchi":
        break
    print(i)
tuple=("apple","orange","mango", "banana", "jackfruit","Litchi")
for x in tuple:
    if x == "Litchi":
        continue
    print(x)


# tuple = (1,2,3)
# for i in tuple:
#     if i == 2:
#         continue
#     print(i)