# def parameter(a,b):
#     return a
# a="hello"
# print(a,str(input("enter your word: ")))

# mistake

# def para(greeting,*name):
#     return greeting
# greeting = "hello"
# g =greeting
# print(parameter(g,str(input("enter your name: ")),str(input("enter your name : "))))

# mistake




def para(a,*b):
    for i in b:
        print(a,i[0])
        print(a,i[1])
para("hello",(str(input("enter your name: ")),str(input("eneter your name: "))))



def para(a,*b):
    for f in b:
        print(a,f[0])
        print(a,f[1])
para(str(input("enetr your greeting: ")),(str(input("enter your num: ")),(str(input("enter your num: ")))))
    