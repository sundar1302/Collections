#Perform Basic Set Operations
A={1,2,3,4} 
B={3,4,5,6}
print(A|B) #Union
print(A&B) #Intersection
print(A-B) #Difference
print(A^B) #Symmetric Difference

A={1,2}
B={1,2,3,4}
print(A.issubset(B)) #Subset

A={1,2,3,4}
B={1,2}
print(A.issuperset(B)) #Superset

A={1,2}
B={3,4}
print(A.isdisjoint(B)) #Disjoint set

#Union of Sets
A={1,2,3,4} 
B={3,4,5,6}
result=A.union(B)
print(result)

#Intersection of Sets
A={1,2,3,4}
B={3,4,5,6}
result=A.intersection(B)
print(result)

#Difference of Sets
A={1,2,3,4}
B={3,4,5,6}
result=A.difference(B)
print(result)

# Symmetric Difference
A={1,2,3,4}
B={3,4,5,6}
result=A.symmetric_difference(B)
print(result)

#Add a list of Elements to a Set
set={1,2,3}
list=[4,5,6]
set.update(list)
print(set)

#Set Difference Update
A={1,2,3,4,5}
B={3,4}
A.difference_update(B)
print(A)

#Remove Items From Set Simultaneously
numbers={1,2,3,4,5,6}
numbers.difference_update({2,4,6})
print(numbers)

#Check Subset
A={1,2}
B={1,2,3,4}
print(A.issubset(B))

#Check Superset
A={1,2,3,4}
B={2,3}
print(A.issuperset(B))

#Set Intersection Check
A={1,2,3}
B={3,4,5}
print(A&B)

#Set Symmetric Difference Update
A={1,2,3,4}
B={3,4,5,6}
A.symmetric_difference_update(B)
print(A)

#Set Intersection Update
A={1,2,3,4}
B={3,4,5,6}
A.intersection_update(B)
print(A)

#Find Common Elements in Two Lists
a=[1,2,3,4,5]
b=[3,4,5,6,7]
c=list(set(a) & set(b))
print(c)

#Frozen Set
fs=frozenset([1,2,3,4])
print(fs)

#Count Unique Words
text="apple banana apple orange banana mango"
words=text.split()
unique=set(words)
print(unique)
print("Count:", len(unique))
