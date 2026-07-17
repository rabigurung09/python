# # A function that calculates the sum of any number of values:
# def cal(*n):
#     total = 0
#     for num in n:
#         total += num
#     return total
# print(cal(int(input("enter your num: ")),int(input("enter your num: "))))
# # def my_function(*numbers):
# #   total = 0
# #   for num in numbers:
# #     total += num
# #   return total

# # print(my_function(1, 2, 3))
# # print(my_function(10, 20, 30, 40))
# # print(my_function(5))

# # Finding the maximum value:
# def max(*num):
#     num_1 = int(input('enter your num: '))
#     for n in num:
#         if n > num_1:
#             print("n is greater:",n)
#         else:
#             print("num_1 is greater:",num_1)
#     return num_1
# max(int(input("enter your num: ")))




def max(*ni):
    maxt = ni[0]
    for num in ni:
        if maxt > num:
            print("the greatest num is : ",n)
    return maxt 
num_1 =int(input("num_1: "))
num_2 =int(input("num_2: "))
num_3 =int(input("num_3: "))
max(num_1,num_2,num_3)
        
    