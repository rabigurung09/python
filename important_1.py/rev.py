# # reverse kathamandu
# city = "kathamandu"
# reverse_city =city[::-1]
# print(reverse_city)


# # using recusive function


# # def city (a):
# #     if len(a) == 0:
# #         return 1
# #     return a[-1:-10:]
# # print(city("kathamandu"))



# string = 'kathamandu'
# def re(index):
#     if index < 0 :
#         return
#     print(string[index],end ="")
#     re (index - 1)
# re(len(string)-1)




str="kathamandu"
def reverse_string(text):
    if text =="":
        return""
    return text [-1]+ reverse_string(text[:-1])
str="kathamandu"
print("reverse mathod: ",reverse_string(str))







