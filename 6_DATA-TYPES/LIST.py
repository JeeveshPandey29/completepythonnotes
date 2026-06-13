#list data type and operations
lst = [10, 20, 30, 40]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#Accessing elements
print(lst[0])      # First element
print(lst[-1])     # Last element
print(lst[1:3])    # Slicing
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#changing elements

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["blackcurrant", "watermelon"]  #change a range of values 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon", "grapes"]
print(thislist) #python can replace one elment with multiple elements

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#adding elements to a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(["grapes", "kiwi"]) #we created a list here
thislist.extend(tropical) #we passed a list here 
print(thislist)

#removing elements
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #only the first occurrence of "banana" is removed

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #removes specified index using pop

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #if do not specify removes the last element 

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #empties the list but the list still exists

#LOOPING THROUGH A LIST

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#SORTING LISTS
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #sorts with uppercase letters first

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#COPY A LIST
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #USING copy() TO COPY A LIST

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)  #USING list() TO COPY A LIST

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #USING SLICING TO COPY A LIST

#JOIN TWO LISTS
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #USING + OPERATOR TO JOIN TWO LISTS 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)  #USING A FOR LOOP TO JOIN TWO LISTS

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  #USING EXTEND() TO JOIN TWO LISTS

#LIST METHODS
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist.count("banana"))  # Count how many times "banana" appears
print(thislist.index("cherry"))  # Find the index of "cherry"





