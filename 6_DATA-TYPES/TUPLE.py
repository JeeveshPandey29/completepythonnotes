#A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)  #note the comma, ye tuple hai kyunki comma hai
print(type(thistuple))

thistuple = ("apple") #ye string aayegi kyunki ek hi elemetn hai
print(type(thistuple))

thistuple = (1) #ye int aayegi
print(type(thistuple))

thistuple = (1,) #ye tuple aayegi kyunki comma hai, agar comma nahi hota toh int aata
print(type(thistuple))

thistuple = (1,2) #ye tuple aayegi kyunki 2 element hai, agar 1 element hota toh int aata
print(type(thistuple))

#a tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#ACCESSING ITEMS IN TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")  #negative indexing 
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #By leaving out the start value, the range will start at the first item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])    #By leaving out the end value, the range will go to the end of the list:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#convert tuple to list add element and convert back to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
newtuple = thistuple + y
print(newtuple)
thistuple += y
print(thistuple)

#convert list to tuple
mylist = ["apple", "banana", "cherry"]
mytuple = tuple(mylist)
print(mytuple)

#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

'''If the number of variables is less than the number of values, you can add an * to the variable name 
# and the values will be assigned to the variable as a list'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#loops
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#maximum and minimum value in a tuple
thistuple = (1, 2, 3, 4, 5)
print(max(thistuple))
print(min(thistuple))

#multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


#METHODS IN TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple.count("apple")) #returns the number of times a specified value occurs in a tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple.index("cherry")) #searches the tuple for a specified value and returns the position of where it was found

