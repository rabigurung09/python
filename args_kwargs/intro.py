# ======args=======
# it helps to accept multiple argument in a single parameter


def arg(*ar):
    print("hello",ar[1])
    print("hello",ar[2])
arg("rabi","ram","shyam")
# output:hello ram
# hello shyam



def argument(para,*arg):
    for args in arg:
      print(para,args)
argument("hello","rabi","shyam")
# output:hello rabi
# hello 



