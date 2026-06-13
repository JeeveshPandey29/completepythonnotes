#DICTIONARY WITH 3 STUDENTS
#A dictionary stores data in key:value pairs.

students = {
    "s1": {
        "name": "Vijay",
        "age": 22,
        "city": "Pune"
    },
    "s2": {
        "name": "Krish",
        "age": 23,
        "city": "Mumbai"
    },
    "s3": {
        "name": "Pandey",
        "age": 24,
        "city": "Delhi"
    }
}

print(students)

#ACCESSING VALUES
students = {
    "s1": {
        "name": "Vijay",
        "age": 22,
        "city": "Pune"
    },
    "s2": {
        "name": "Krish",
        "age": 23,
        "city": "Mumbai"
    },
    "s3": {
        "name": "Pandey",
        "age": 24,
        "city": "Delhi"
    }
}

print(students["s1"]["name"])    # Vijay
print(students["s2"]["age"])     # 23
print(students["s3"]["city"])    # Delhi

#GET METHOD
print(students["s1"].get("name"))
print(students["s2"].get("age"))

#GET ALL KEYS
print(students.keys())

#GET ALL VALUES
print(students.values())

#GET ALL ITEMS
print(students.items())

#CHECK IF KEY EXISTS
if "s1" in students:
    print("Student Exists")

#LENGTH OF DICTIONARY
print(len(students))

#ADD NEW STUDENT
students["s4"] = {
    "name": "Aditya",
    "age": 25,
    "city": "Nashik"
}

print(students)

#UPDATE STUDENT DATA
students["s1"]["age"] = 23
print(students)

#UPDATE USING update()
students["s2"].update({"city": "Pune"})
print(students)

#ADD NEW FIELD
students["s1"]["college"] = "MIT-WPU"
print(students)

#REMOVE FIELD
students["s1"].pop("city")
print(students)

#REMOVE LAST STUDENT
students.popitem()
print(students)

#DELETE STUDENT
del students["s3"]
print(students)

#LOOP THROUGH STUDENT IDS
for x in students:
    print(x)

#LOOP THROUGH STUDENT DETAILS
for student_id, details in students.items():
    print(student_id, details)

#LOOP THROUGH NESTED DICTIONARY
for student_id, details in students.items():

    print(student_id)

    for key, value in details.items():
        print(key, ":", value)

    print()

#COPY DICTIONARY
new_students = students.copy()
print(new_students)

#COPY USING dict()
new_students = dict(students)
print(new_students)

#FROMKEYS METHOD
keys = ("name", "age", "city")
value = "Not Available"

d = dict.fromkeys(keys, value)
print(d)

#SETDEFAULT METHOD
students["s1"].setdefault("country", "India")
print(students)

#GET METHOD
print(students["s1"].get("name"))
print(students["s1"].get("salary"))
print(students["s1"].get("salary", 0))

#PRACTICAL EXAMPLE
students = {
    "s1": {
        "name": "Vijay",
        "skills": ["Python", "Java"]
    },
    "s2": {
        "name": "Krish",
        "skills": ["Cybersecurity", "Linux"]
    },
    "s3": {
        "name": "Pandey",
        "skills": ["C++", "DSA"]
    }
}

print(students["s1"]["name"])
print(students["s2"]["skills"][0])
print(students["s3"]["skills"][1])

#COMMON DICTIONARY METHODS
print(students.keys())
print(students.values())
print(students.items())

students.update({
    "s4": {
        "name": "Aditya",
        "skills": ["Cloud", "AWS"]
    }
})

print(students)

students.pop("s4")
print(students)

students.clear()
print(students)