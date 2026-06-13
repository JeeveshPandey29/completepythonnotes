'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''

f = open("demofile.txt")
f = open("demofile.txt", "rt") #this code is same as the above

f = open("demofile.txt")
print(f.read()) #to read the content of the file 

#If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())

f = open("demofile.txt")
print(f.readline())
f.close()  #always close a file 

with open("demofile.txt") as f:
  print(f.read(5)) #return the first 5 characters

with open("demofile.txt") as f:
  print(f.readline()) #read oneline of the file

#loop thorugh the file line by line
with open("demofile.txt") as f:
  for x in f:
    print(x)

#write-create files
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
with open("demofile.txt") as f: #open and read the file after the appending:
  print(f.read())

#overwriting in a file
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
with open("demofile.txt") as f: #open and read the file after the overwriting:
  print(f.read())

#create a new file
f = open("myfile.txt", "x")

#delete a file 
import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder") #remove folder

