#ARITHMETIC OPERTORS 
a, b = 10, 3
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

#ASSIGNMENT OPERATORS
a = 5

a += 3   # Addition assignment (a = a + 3)
print(a)

a -= 3   # Subtraction assignment (a = a - 3)
print(a)

a *= 3   # Multiplication assignment (a = a * 3)
print(a)

a /= 3   # Division assignment (a = a / 3)
print(a)

a %= 3   # Modulus assignment (a = a % 3)
print(a)

a //= 3  # Floor Division assignment (a = a // 3)
print(a)

a **= 3  # Exponentiation assignment (a = a ** 3)
print(a)

a &= 3   # Bitwise AND assignment (a = a & 3)
print(a)

a |= 3   # Bitwise OR assignment (a = a | 3)
print(a)


#TERNARY OPERATOR
a, b = 10, 20
min_val = a if a < b else b
print(min_val) # Outputs 10

#COMPARISON OPERATORS
a, b = 10, 20
print(a > b) # Greater than
print(a < b) # Less than
print(a == b) # Equal to
print(a != b) # Not equal to
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

#LOGICAL OPERATORS
a, b = True, False
print(a and b) # Logical AND
print(a or b) # Logical OR
print(not a) # Logical NOT

#IDENTITY OPERATORS
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # True
print(a is not c) # True

#MEMBERSHIP OPERATORS
my_list = [1, 2, 3, 4]
print(3 in my_list) # True
print(5 not in my_list) # True

#BITWISE OPERATORS
a, b = 10, 4
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(~a) # Bitwise NOT
print(a ^ b) # Bitwise XOR
print(a >> 2) # Right shift
print(a << 2) # Left shift


#NONE
x = None
print(x)
print(type(x))

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")


print(bool(None)) #false

def myfunc():
  x = 5    #a function without a return statement returns none
x = myfunc()
print(x)