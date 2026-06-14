# ====add()==== it add the element to the set
# syntax:var.add(element)
myset={1,55.5,"ram","shyam"}
myset_1={"orange","apple"}
myset.add("shyam")
print(myset)
# output:{'ram', 1, 'shyam', 55.5}
myset_1.add(5)
print(myset_1)
# output:{'orange', 'apple', 5}
# ====update()====it update the set by adding value to the set
myset_3={1,55.5,"ram","shyam"}
myset_3.update({"rabi"})
print(myset_3)
# output:{'orange', 'apple', 5}
myset_1.update({"banana"})
# output:{1, 'shyam', 'rabi', 55.5, 'ram'}
# =====remove()=== 
# it removes the element of set
myset_1={"orange","apple"}
myset_1.remove("orange")
print(myset_1)
# output:{'apple'}#it will give key error if the value is not in the set
# =====discard()====it will give none if the value is not found and if the value is found it will discard the value
myset_1={"orange","apple"}
myset_1.discard("orange")
print(myset_1)
# output:{'apple'}#it will give none if the value is not found
# =======pop()======
myset_1={"orange","apple"}
myset_1.pop()
print(myset_1)
# output:it remove value of set randomly
# ======clear()=======
# it clear all the value of set
myset_1={"orange","apple"}
myset_1.clear()
print(myset_1)
# output:set()
# =======union====
# it contains all the element inside two set
myset_1={"orange","apple",55.5}
myset={1,55.5,"ram","shyam"}
print(myset_1.union(myset))
print(myset_1|myset)#(|) or operator ,output:{1, 'shyam', 55.5, 'orange', 'ram', 'apple'}
# output:{1, 'shyam', 55.5, 'orange', 'ram', 'apple'}
# ======intersection()======it gives all the same value sets
# it contain only comman element from two set
myset_1={"orange","apple",55.5,1}
myset={1,55.5,"ram","shyam"}
print(myset_1.intersection(myset))
print(myset_1 & myset)#(&)and operator
# output:{1, 55.5}
# ========difference====
# in two difference set are given then the first difference from secind set .so it contain only first set element and removes all value inside set 2
myset_1={"orange","apple",55.5,1}
myset={1,55.5,"ram","shyam"}
myset.difference(myset_1)
print(myset.difference(myset_1))
print(myset - myset_1)
# output:{'shyam', 'ram'}
