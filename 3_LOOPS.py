#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

#With the break statement we can stop the loop even if the while condition is true:
i = 1   #Exit the loop when i is 3:
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#print when the condition becomes false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#range(start,stop,step)
print(list(range(5)))  #[0, 1, 2, 3, 4]
print(list(range(1, 6)))  #[1, 2, 3, 4, 5]
print(list(range(5, 20, 3)))  #[5, 8, 11, 14, 17]

for x in range(6):
  print(x)

for x in range(2, 30, 3): #increment the sequence with 3
  print(x)

