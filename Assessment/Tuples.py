#Perform Basic Tuple Operations
t=(1,2,3,4,5)  #Create tuple
print(t)

print(t[0]) #Access elements
print(t[4])

print(t[2:4]) #Slicing a tuple
print(len(t)) #length

t1=(1, 2) #concatenate tuples
t2=(3, 4)
result=t1+t2
print(result)

t=(10,20,30) #tuple unpacking
a,b,c=t
print(a,b,c)

t=(1,2,3) #convert tuple to list
list=list(t)
list.append(4)
t=tuple(list)
print(t)

#Tuple repetition
t=(1,2,3)
result=t*3
print(result)

#Slicing Tuples
t=(10,20,30,40,50)
print(t[1:4])

#Reverse the tuple
t=(1,2,3,4,5)
print(t[::-1])

#Access Nested Tuples
nested = ("apple", ("banana", "orange", "grape"), "mango")
print(nested[1][2])

#Create a tuple with single item 50
t = (50,)
print(t)

#Unpack the tuple into 4 variables
t=(10,20,30,40)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)

#Swap two tuples in Python
t1=(1,2,3)
t2=(4,5,6)
t1,t2=t2,t1
print(t1)
print(t2)

#Copy specific elements from tuple
t=(10,20,30,40)
value=(t[0],t[2],t[3])
print(value)

#List to Tuple
list=[10,20,30,40]
TupleVal=tuple(list)
print(TupleVal)

#Function returning tuple
def values():
    return(10,20,30)
result=values()
print(result)

#Comparing Tuples
t1=(1,2,3)
t2=(1,2,3)
print(t1==t2)

#Removing Duplicates from Tuple
t=(1,2,3,3,4,4,1)
remove=tuple(set(t))
print(remove)

#Filter Tuples
t=(10,25,30,45,50)
filter=()
for x in t:
    if x>30:
        filter+=(x,)
print(filter)

#Map Tuples
t=(1,2,3,4,5)
result=tuple(map(lambda x: x * 2, t))
print(result)

#Modify Tuple
t=(1,2,3)
t=t+(4, 5)
print(t)

#Sort a tuple of tuples by 2nd item
t=((1, 5),(3, 2),(4, 8),(2, 1))
sorted_t=tuple(sorted(t, key=lambda x: x[1]))
print(sorted_t)

#Count Elements
t=(1,2,3,3,4,2,1)
print(t.count(2))

#Check if all items in the tuple are the same
t=(5,5,5)
result=t.count(t[0])==len(t)
print(result)