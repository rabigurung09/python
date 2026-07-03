"""
    =======while=====
    while loop execute a set of code as long as condition is true
    while loop and for loop is two primitive loop
    while loop is used to repate (execute ) block if code until condition become false
    
    
    """
i = 1
while i < 6:
    print(i)
    i+=1

# output:1
# 2
# 3
# 4
# 5
i =0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# output:1
# 2
# 4
# 5
# 6
# Note that number 3 is missing in the result
name="ram"
i=0
while i < len(name) :
    print(name[i])
    i=i+1
# output=  
# r
# a
# m