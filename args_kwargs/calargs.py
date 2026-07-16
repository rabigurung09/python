# A function that calculates the sum of any number of values:
def cal(*n):
    total = 0
    for num in n:
        total += num
    return total
print(cal(int(input("enter your num: ")),int(input("enter your num: "))))
# def my_function(*numbers):
#   total = 0
#   for num in numbers:
#     total += num
#   return total

# print(my_function(1, 2, 3))
# print(my_function(10, 20, 30, 40))
# print(my_function(5))