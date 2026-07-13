result = lambda a , b: a * b
print(result(23,3))
# output:69

output = lambda a ,b: a**b
print(output(3,3))
# output:27




result = lambda a:a**2
print(result(3))
# output:9


def output (n):
    return lambda a: a + n
ero = output(1)
print(ero(4))