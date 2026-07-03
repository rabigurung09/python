# set
# set is a collection of data (element) which is in unorderd form snd doesnt allow the duplicate element(it automatically remove duplicate items)0
# it is a mutable data type so we can change,remove,update the value of set
# the value inside set is always unique (without duplicate)
# example
myset=set()
print(type(myset))
# output :<class 'set'>
# we can create empty set using set function
myset={"saroj",55.4,1,1,True,}
print(type(myset))
# output:{1, 'saroj', 55.4}
# write a program to create empty set and then take data from user  and keep it inside the set and print it into terminal
set=set()
user_1=input("enter your name")
user_2=int(input("enter YOUR age"))
user_3=float(input("enter your weigh"))
set.add(user_1)
set.add(user_2)
set.add(user_3)
print(set)
