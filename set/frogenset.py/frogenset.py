# # frogen set is an immuitable (unchangable)set in python whose 
# element cannot be addded ,removed ,or modifaction after creation
# when we write element inside frogen set then it must be in string list ,tuple etc. 
# exampleL:
myfruit=frozenset({"saroj",1,"ram","orange"})
print(myfruit)
print(type(myfruit))
# output:frozenset({1, 'ram', 'saroj', 'orange'})
# <class 'frozenset'>
num=frozenset({'saroj'})
print(num)
# output:frozenset({'saroj'})
print(len(num))
# output:1
lst=frozenset(["saroj",2,3,"orange"])
print(lst)
# # output:frozenset({2, 3, 'orange', 'saroj'})
tup =frozenset((1,2,"ram"))
print(tup)
# output:frozenset({1, 2, 'ram'})
"""q.1.given set is 
details={1,"saroj","ktm"}
write a programto add 50 into the given set"""
details={1,"saroj","ktm"}
details.add(50)
print(details)
# output:{1, 'saroj', 50, 'ktm'}

"""q.n2.write a program to your 3 friend name as input from user, and finally add them into the set name "friends.
note:using add() function and also check its data type"""
friends=set()
user_1=input("enter your name : ")
user_2=input("enter your name : ")
user_3=input("enter your name : ")
friends.add(user_1)
friends.add(user_2)
friends.add(user_3)
print(friends)


