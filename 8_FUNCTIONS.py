# functions are block of code that can be called multiple times without code repetition.
def mit ():
    print("python is good")   

def mit2():
    return "Python is not good" 

# mit() prints the text, but the function itself returns None

def add():
    a = 2
    b= 3
    c = a +b
    print(c)

add()

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
  pass

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.


def fruit(name):
    print("i like", name)
fruit("Mango")

# function with parameter without return
def add(a, b):
    c = a+b
    print(c)
add(10,20)

# function with parameter with return
def add(a,b):
    return (a+b)
print(add(2, 4))

# function without parameter without return
def add():
    a = 2
    b=3
    c = a+b
    print (c)

# function without parameter and with return 
def add():
    a = 10
    b= 20
    return a+b

# Q. passing list as an argument
def listpass(items):
    for i in items:
        print (i)
    print(len(items))

list = [1, 2, 3]
listpass(list)

def fruit(*fruitlist):
    print(fruitlist[0])
fruit("mango", "apple", "banana")

def fruit(*fruitlist):
    print(fruitlist[0])
fruit = ("mango", "apple", "banana") #here fruit is assigned to tuple function revoked; nothing will be printed

#table of any number using recursion
def table (no):
    if no < 50:
        print(no)
    no = no  + 5
    table(no)
print(5)

#factorial of any number using recursion
def factorial(m):
    if m == 0 or m == 1:
        return 1
    else:
        return (m * factorial(m-1))
print(factorial(5))

# def factorial(m):
#     if m == 0 or m == 1:
#         print(1) 
#     else:
#         print((m * factorial(m-1)))
# factorial(5) #error beacuse selected 5 goes into else block 5 * factorial(4) but then it prints and does not return back as return is not used.