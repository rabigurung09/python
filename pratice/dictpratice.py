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
"""9.	Create a dictionary using fromkeys() with keys:"""
de={
    "name":"rabi",
    "class":"bachlor",
    "age":3
    
}
key=["name","class","age"]
det=de.fromkeys(key,0)
print(det)
"""10.	Use setdefault() to add a faculty key if it does not exist
"""
dt={
    "name":"resham",
    "class":"bachlor",
    "roll":1
}
df=dt.setdefault("email","rabi23@gmail.com")
print(dt)
# output:{'name': 'resham', 'class': 'bachlor', 'roll': 1, 'email': 'rabi23@gmail.com'}
"""11.	Add a new student to a nested dictionary."""
dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
# output:{'oldstudent': {'name': 'ram', 'age': 12}, 'newstudent': {'name': 'shyam', 'age': 21}}
"""12.	Update Hari's age from 21 to 22."""
name={
    "firstname":"hari",
    "age":21
}
name["age"]=23
print(name)
# output:{'firstname': 'hari', 'age': 23}
"""13.	Remove student s1 from the nested dictionary."""
dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
txt=dp.popitem()
print(dp)
# output:{'oldstudent': {'name': 'ram', 'age': 12}}
"""14.	Add GPA to student s1."""
dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
txt=dp.popitem()
print(dp)
te=dp.get("oldstudent")["gpa"]=4
print(dp)
# output:{'oldstudent': {'name': 'ram', 'age': 12, 'gpa': 4}}
"""15.	Display only the age of student s2."""
dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
txt=dp.get("oldstudent")["age"]
print(txt)
# output:12
"""16.	Replace Ram's name with Shyam."""

dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
txt=dp.popitem()
print(dp)
te=dp.get("oldstudent")["gpa"]=4
print(dp)
tr=dp.get("oldstudent")["name"]="shyam"
print(dp)
# output:{'oldstudent': {'name': 'shyam', 'age': 12, 'gpa': 4}}
"""17.	Add a new subject key inside student s1."""

dp={
    "oldstudent":{
        "name":"ram",
        "age":12
    },
    
}
dp["newstudent"]={
    "name":"shyam",
    "age":21
    
}
print(dp)
txt=dp.popitem()
print(dp)
te=dp.get("oldstudent")["gpa"]=4
print(dp)
tr=dp.get("oldstudent")["name"]="shyam"
print(dp)
dp.get("oldstudent")["number"]=984366286
print(dp)
# output:{'oldstudent': {'name': 'shyam', 'age': 12, 'gpa': 4, 'number': 984366286}}
