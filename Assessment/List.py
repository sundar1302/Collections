# Basic List Operations
#Create a List
numbers=[20,25,55,65,45,66]
print(numbers)
print(numbers[3]) #Access Elements
print(numbers[5]) #Access Elements
numbers.append(33)
print(numbers)
numbers.insert(2,22)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.pop(2)
print(numbers)
numbers[1]=35
print(numbers)
print(len(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[1:4])
del numbers[1]
print(numbers)
numbers.extend([33])
print(numbers)
print(numbers.count(33))

#concatenate
number=[10,12,14]
numbers=[16,18,20]
result=number+numbers
print(result)

#Sum and Average of all numbers
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum =", total)
print("Average =", average)

#Reverse a list 
numbers = [1,2,3,4,5]
reverse = numbers[::-1]
print(reverse)

#Square the numbers in list
numbers = [2,4,6,8,10]
squares = [num ** 2 for num in numbers]
print(squares)

#Maximum and Minimum numbers
numbers=[10,12,22,6,55]
print(max(numbers))
print(min(numbers))

#Count Occurences
numbers = [1,2,3,2,2,4]
count = numbers.count(2)
print(count)

#Sort a list of numbers
numbers=[1,7,3,5,7,9]
numbers.sort()
print(numbers)

#Copy of a list
numbers=[10,20,30,40]
copy=numbers.copy()
print(copy)

#Combine two list
list1=[1,2,3]
list2=[4,5,6]
result=list1+list2
print(result)

#Remove empty strings
strings=["sundar","","vikram","","ro","ko"]
remove=[s for s in strings if s != ""]
print(remove)

#Remove duplicates
numbers=[1,2,2,5,4,4,5]
duplicate=list(set(numbers))
print(duplicate)

#Remove all occurrence of specific item
numbers=[1,2,3,2,4,2,5]
result=[num for num in numbers if num != 3]
print(result) 

#List Comprehension for Numbers
numbers=[x for x in range(1, 11)]
print(numbers)

#Access nested list
data=[[10, 20, 30],[40, 50, 60],[70, 80, 90]]
print(data[0])
print(data[1])
print(data[0][2])
data[2][2]=100
print(data)

#Flatten Nested List
nested=[[1, 2],[3, 4],[5, 6]]
flattened = []
for sublist in nested:
    flattened.extend(sublist)
print(flattened)

#Concatenate two list index-wise
list1=[1, 2, 3]
list2=['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)

#Iterate both list simultaneously
list1=[1, 2, 3]
list2=['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)

#Add new item to list after a specified item
numbers=[10, 20, 30, 40]
numbers.insert(numbers.index(20)+ 1,25)
print(numbers)

#Extend nested list by adding the sublist
nested=[[1, 2], [3, 4]]
new_sublist=[5, 6]
nested.append(new_sublist)
print(nested)

#Replace list’s item with new value if found
fruits=["apple","banana","orange","kiwi"]
if "banana" in fruits:
    fruits[fruits.index("banana")] = "grape"
print(fruits)

