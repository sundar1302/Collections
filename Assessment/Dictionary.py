#Perform basic dictionary operations
student={"name":"sundar","age":25,"City":"Chennai"} #Create dictionary
print(student)

print(student["name"]) #Access values
print(student.get("age"))

student["age"]=21 #update
student["Education"]="B.E" #add new key
print(student)

student.pop("City") #remove items
print(student)

del student["age"] #using del
print(student)

print(student.keys())
print(student.values())
print(student.items())

student.clear() #clear dictionary
print(student)

d1={"a": 1, "b": 2}
d2={"c": 3} #merge dictionary
d1.update(d2)
print(d1)

#Dictionary from list
keys=["name", "age", "city"]
values=["sundar", 25, "Chennai"]
result = dict(zip(keys, values))
print(result)

#Clear dictionary
student={"name":"Sai","age":20,"city":"Kanchi"}
student.clear()
print(student)

#Merge dictionary
d1={"a": 1, "b": 2}
d2={"c": 3, "d": 4}
d1.update(d2)
print(d1)

#Count character freq
text="sundar"
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

#Access nested dictionary
student={"name":"Shan","details":{"age":28,"course":"Python"}}
print(student["name"])             
print(student["details"]["course"])

#Print the value of key ‘history’ from nested dict
student = {"name": "sundar","marks":{"math":70,"history":75}}
print(student["marks"]["history"])

#Modify nested dictionary
student = {"name": "Sundar","marks":{"math":90,"history":85}}
student["marks"]["history"]=95
print(student["marks"]["history"])

#initialize dictionary with default values
keys=["a","b","c"]
d = dict.fromkeys(keys, 5)
print(d)

#Create a dictionary by extracting the keys from a given dictionary
original={"a": 1, "b": 2, "c": 3}
new={key:10 for key in original}
print(new)

#Delete a list of keys from a dictionary
student={"a":1,"b":2,"c":3,"d":4}
remove=["a","c"]
for key in remove:
    if key in student:
        del student[key]
print(student)

#Check if a value exists in a dictionary
student={"a":1,"b":2,"c":3}
if 3 in student.values():
    print("Value exists")
else:
    print("Error")

#Rename key of a dictionary
student={"name":"sundar","age":30}
student["full_name"]=student.pop("name")
print(student)

#Get the key of a minimum value
data={"a":10,"b":3,"c":7}
minimum=min(data,key=data.get)
print(minimum)

#Change value of a key in a nested dictionary
stud={"name":"sundar","marks":{"maths":70,"science":85}}
stud["marks"]["science"] = 95
print(stud)

#Invert Dictionary
data={"a":1,"b":2,"c":3}
invert=dict(zip(data.values(),data.keys()))
print(invert)

#Sort Dictionary by Keys
data={"b":2,"a":1,"c":3}
sort=dict(sorted(data.items()))
print(sort)

#Sort Dictionary by Values
data={"a":3,"b":1,"c":2}
sortValues=dict(sorted(data.items(),key=lambda x: x[1]))
print(sortValues)

#Check if All Values are Unique
data={"a":1,"b":2,"c":2}
if len(data.values())==len(set(data.values())):
    print("All values are unique")
else:
    print("Duplicates found")


