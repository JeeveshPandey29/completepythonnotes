#a set is changeable but it is unordered and does not allow duplicate values. It is defined by placing the items inside curly braces {} separated by commas or by using the built-in set() function.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#duplicates are not allowed in sets.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#true and 1 are considered as same values
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#similarly false and 0 are considered as same values
thisset = {"apple", "banana", "cherry", False, 0, 1}
print(thisset)  

#length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#set can have different data types
set1 = {"abc", 34, True, 40, "male"}

#data type of a set
myset = {"apple", "banana", "cherry"}
print(type(myset))

#2nd way to print set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#accessing items in a set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#if item not present remove() will raise an error but discard() will not raise an error

#pop will remove one random element from the set and return it.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#looping through a set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#JOINING SETS
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#join multiple sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#join a set and a tuple 
x = {"a", "b", "c"}
y = (1, 2, 3)
print(x.union(y))

#update it changes the originla set and do not return a new set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Question: difference in union and update ??

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#frozen set is a set that is immutable. Once created, you cannot change its items, add new items, or remove existing items.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#superset is a set that contains all the elements of another set. The issuperset() method returns True if the set is a superset of the specified set, otherwise it returns False.
setA = {"apple", "banana", "cherry"}
setB = {"apple", "banana"}
print(setA.issuperset(setB))   # True
print(setB.issuperset(setA))   # False

setA = {"apple", "banana", "cherry"}
setB = {"apple", "banana"}
print(setA>=(setB))   # True
print(setB>=(setA))   # False

'''setA <= setB → equivalent to setA.issubset(setB)
setA >= setB → equivalent to setA.issuperset(setB)
setA < setB → proper subset (all elements in setA are in setB, but setB has more)
setA > setB → proper superset (all elements in setB are in setA, but setA has more)'''

