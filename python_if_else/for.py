"""
====for loop====

In Python, a for loop is used to iterate over a sequence 
(like a list, tuple, string, dictionary, or range) and execute a block of code for each item in that sequence.
# Iterative means repeating a process step by step until a condition is met.


"""
a = ["apple","banana","mango"]
for cat in a:
    print(cat)
# output=apple
# banana
# mango
for dog in "promation":
    print(dog)
# output=p
# r
# o
# m
# a
# t
# i
# o
# n
   

# ========break_satement=====
fruits=["appple","guava","litchy"]
for y in fruits:
    print(y)
    if y=="guava":
        break
# output=appple
# guava
color=["red","blue","yellow"]
for d in color:
    if d=="blue":
        break
        print(d)
# output=red
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
