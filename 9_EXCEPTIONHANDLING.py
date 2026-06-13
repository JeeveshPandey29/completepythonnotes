# try block: it will execute only when all things correct 
# except: it will execute when theree will be error
#else: execute when no error: try + else ek sath execute ho jayenge 
#finally: error ho na ho ye to execute hoga hi 

try:
  x = 3
  print(x)
except:
  print("An exception occurred")  #isme try execute and print hoga 

try:
  print(y)
except:
  print("An exception occurred")  #isme except print hoga 


try:
  print(w)
except NameError:
  print("Variable w is not defined")
except:
  print("Something else went wrong") #w defined nahi hai islie error try  block execute hoga

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") #try and else print hoga 

try:
  print(p)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") #p not defined islie except execute hoga



try:
  print(g)
except:
  print("Something went wrong")
else:
  print("try sahi hua to print ho jaunga")
finally: 
  print("The 'try except' is finished")   #g not defined to try but finally block  bhi hai to wo  bhi hoga 

try:
  print(x)
except:
  print("Something went wrong")
else:
  print("try sahi hua to print ho jaunga")
finally:
  print("The 'try except' is finished") #try else finally sab execute ho gaye 


try:
  a = 5
  b = 0
  c = a/b
except:
  print("error")
else:
  print("ho gya print")
finally:
  print("Khel khtm")
