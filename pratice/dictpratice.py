""" ===============dictonary question=================
1.	Create a dictionary with name, age, and city. Add a new key gpa."""
dictonary={
    "name":"rabi",
    "age":12,
    "city":"ktm",
}
dictonary["gpa"]=4
print(dictonary)
# output:{'name': 'rabi', 'age': 12, 'city': 'ktm', 'gpa': 4}
"""2.	2. Create a dictionary and update the age from 22 to 23."""
dict={
    "name":"rabi",
    "age":22
}
dict["age"]=23
print(dict)
# output:{'name': 'rabi', 'age': 23}
"""3.	Remove the city key from a dictionary."""
dic={
    "name":"rabi",
    "age":3,
    "city":"ktm"
    
}
dic.pop("city")
print(dic)
# output:{'name': 'rabi', 'age': 3}
"""4.	Take a key from the user and display its value using """
di={
    "name":"ram",
    "age":3,
    "city":"ktm",
}
user=input("enter a key")
text=dic.get(user)
print(text)
"""5.	Add multiple new keys (email, phone) using update()."""
d={
    "name":"rabi",
    "age":3,
    
}
d.update({"email":"rau234@gmail.com"})
print(d)
# output:{'name': 'rabi', 'age': 3, 'email': 'rau234@gmail.com'}
d.popitem()
print(d)
# output:{'name': 'rabi', 'age': 3}
"""7.	Copy a dictionary and add a new key in the copied dictionary."""
diy={
    "name":"ram",
    "salary":2000
}
re=diy.copy()
re["city"]="ktm"
print(re)
# output:{'name': 'ram', 'salary': 2000, 'city': 'ktm'}
""'8.	Clear all records from a dictionary.'""
dit={
    "name":"shyam",
    "adventure":"everestbasecamp"
}
dit.clear()
print(dit)
# output:{}