student={
    "cource":"bca",
    "roll_no1":{
        "name":"rabi",
        "skill":"python",
        "age":20
        
    },
    "roll_no2":{
        "name_1":"ram",
        "skill":"python with django",
        "height":5.4
        
    }
    
    
}
print(student.get("roll_no1").get("name"))
student.get("roll_no1").update({"name":"shyam"})
print(student)
INFO={
    "course":"bca",
    "roll_no1":{
        "name":"ram",
        "age":20,
        "marks":[10,20,30,40]
        
    },
    "roll_no2":{
         "name":"shyam",
        "age":35,
        "marks":[10,20,40,50]
        
    }
}

print(INFO.get("roll_no2").get("marks"))
INFO.get("roll_no2").get("marks")[3]=30

print(INFO)
print(INFO.get("roll_no2").get("marks"))
instagram={
    "name":"rabi",
    "folling":{
        "follwer":280,
        "follwing":110
    },
    "reals":{
        "folling_reals":[1,2,23,3,4,45,5]
    }
}
print(instagram.get("folling").get("follwer"))
instagram.get("reals").get("folling_reals").sort()
print(instagram)
instagram.get("reals").get("folling_reals")[5]=6
print(instagram)
instagram.get("reals").get("folling_reals")[6]=7
print(instagram)
print(instagram.get("reals").get("folling_reals"))
instagram={
    "name":"rabi",
    "folling":{
        "follwer":280,
        "follwing":110
    },
    "reals":{
        "folling_reals":[1,2,23,3,4,45,5]
    }
}
text=instagram.setdefault("ram")
print(text)
# my_dictionary={
#     "apple":123,
#     "orange":567,
#     "student":"id",
#     "roll_no":5
# }
# user=input("enter variable name : ")
# print(my_dictionary.get(user,"word not found"))
# output:enter variable name : appla
# word not found
# enter variable name : orange
# 567
english_nepali_dict = {
    "Apple": "स्याउ",
    "Book": "पुस्तक",
    "Cat": "बिरालो",
    "Dog": "कुकुर",
    "House": "घर",
    "School": "विद्यालय",
    "Teacher": "शिक्षक",
    "Student": "विद्यार्थी",
    "Water": "पानी",
    "Food": "खाना",
    "Sun": "घाम",
    "Moon": "चन्द्रमा",
    "Star": "तारा",
    "Tree": "रुख",
    "Flower": "फूल",
    "Road": "बाटो",
    "Car": "गाडी",
    "Bus": "बस",
    "Chair": "कुर्सी",
    "Table": "टेबल"
}
user=input("ENTERE a value for meaning : ").title()
print(english_nepali_dict.get(user,"word not found"))

