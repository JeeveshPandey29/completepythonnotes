class college:
    A = "Mit"

B = college()
print(college.A)
print(B.A)

# When you create an object from a class, it inherits all the variables and functions defined inside that class.

del B

# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
#  in the pass statement to avoid getting an error.

class Person:
  pass


class students:
   name = "Jeevesh Pandey"
   roll = 33

s1 = students()
print(s1.name, s1.roll)
print(s1.roll)

# self keyword in function refer to objects of same class. 
 
class teacher:
   name="random"
   tid = 123
   def info(self):
      print(self.name)
      print(self.tid)

s1= teacher()
s1.info()  


# inheritance (single level)
class rectangle:
   def rectarea(self, length, breadth):
      area = length * breadth
      print("single inheritance rectarea", area)

class square(rectangle):
   def sqarea(self, side):
      area = side * side
      print("single inheritance sq area", area)

obj = square()
obj.rectarea(5, 4)
obj.sqarea(5)

print (" ")

# multple inheritance

class rectangle:
   def rectarea(self, length, breadth):
      area = length * breadth
      print("multiple inheritance rectarea", area)

class square():
   def sqarea(self, side):
      area = side * side
      print("multiple inheritance sqarea",area)

class traingle (rectangle, square):
   def tarea(self, base, height):
      area = 0.5 * base * height
      print("multiple inheritance trea",area)

obj = traingle()
obj.tarea(5, 10)
obj.sqarea(5)
obj.rectarea(4, 5)

print (" ")

# multilevel inheritance
class rectangle:
   def rectarea(self, length, breadth):
      area = length * breadth
      print("multilevel inheritance rectarea", area)

class square(rectangle):
   def sqarea(self, side):
      area = side * side
      print("multilevel inheritance sq area", area)

class circle(square):
   def carea(self, radius):
      area = 3.14 * radius * radius
      print("Multilevel inheritance circle area", area)

obj = circle()
obj.carea(7)
obj.sqarea(5)
obj.rectarea(4, 5)

print (" ")

# hierarchial inheritance
class rectangle:
   def rectarea(self, length, breadth):
      area = length * breadth
      print("hierarchial inheritance rectarea", area)

class square(rectangle):
   def sqarea(self, side):
      area = side * side
      print("hierarchial inheritance sq area", area)

class circle(rectangle):
   def carea(self, radius):
      area = 3.14 * radius * radius
      print("hierarchial inheritance circle area", area)

obj1 = circle()
obj2 = square()
obj1.carea(7)
obj2.sqarea(5)
obj1.rectarea(4, 5)
obj2.rectarea(6, 5)

print (" ")

# hybrid inheritance
class rectangle:
   def rectarea(self, length, breadth):
      area = length * breadth
      print("hybrid inheritance rectarea", area)

class square(rectangle):
   def sqarea(self, side):
      area = side * side
      print("hybrid inheritance sq area", area)

class circle():
   def carea(self, radius):
      area = 3.14 * radius * radius
      print("hybrid inheritance circle area", area)

class traingle (circle, square):
   def tarea(self, base, height):
      area = 0.5 * base * height
      print("hybrid inheritance trea",area)

obj = traingle()
obj.sqarea(7)
obj.rectarea(4, 5)
obj.tarea(5, 10)
obj.carea(5)

print(" ")

# public access modifier
class Public:
   def __init__ (self):
      self.name = "Jeevesh"

   def displayname(self):
      print(self.name)

obj = Public()
obj.displayname()
print(obj.name)

class Protected :
   def __init__(self):
      self.age = 30

class subclass(Protected):
   def displayage(self):
      print(self.age)

obj = subclass()
obj.displayage()

#polymorphism

class shape:
   def area(self):
      return "Undefned"
   


#polymorphism means same operation different beahviour. it allows functions  or methods with same name to
# work differently depending on the 

# data abstraction hide the internal implementation details while exposing only thenecceessary funcntionlality. it helps focus on 
# "what to do" rather than "how to do it". 

