a = "Hello"
print(a)

a = "Hello, World!"
print(a[1])

#looping through a string
for x in "banana":
  print(x)

#length of a string
a = "Hello, World!"
print(len(a))

#check in a string 
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not in a string
txt = "The best things in life are free!"
print("expensive" not in txt)

#SLICING
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

#METHODS
a = "Hello, World!"     
print(a.upper())            #uppercase

a = "Hello, World!"
print(a.lower())            #lowercase

a = " Hello, World! "
print(a.strip())            # returns "Hello, World!" remove extra spaces

txt = "     hello world     "
print(txt.lstrip()) #removes leading spaces

txt = "     hello world     "
print(txt.rstrip()) #removes trailing spaces

a = "Hello, World!"
print(a.replace("H", "J")) #replace string

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#CONCATENATING STRINGS
a = "Hello"
b = "World"
c = a + b
print(c)

#ESCAPE CHARACTERS
print("It\'s a test")       # Single quote
print("Path: C:\\Users")    # Backslash
print("Line1\nLine2")       # New line
print("Hello\tWorld")       # Tab space
print("ABC\bD")             # Backspace removes C → ABD
print("\101")               # Octal → A
print("\x41")               # Hex → A

#CASE CONVERSION
txt = "hello world"
print(txt.capitalize())   # Hello world
print(txt.casefold())     # hello world (lowercase, more aggressive than lower())
print(txt.lower())        # hello world
print(txt.upper())        # HELLO WORLD
print(txt.title())        # Hello World
print(txt.swapcase())     # HELLO WORLD → hello world


#ALIGNMENT AND FORMATTING
txt = "    apple" 
print(txt.center(10))     # '  apple   ' (centered in width 10)

txt = "    apple"
print(txt.ljust(10))      # 'apple     ' (left justified)

txt = "    apple"
print(txt.rjust(10))      # '     apple' (right justified)

txt = "    apple"
print(txt.zfill(10))      # '000000apple' (pads with zeros)


#SEARCHING 
txt = "banana banana"
print(txt.count("na"))    # 4 (occurrences)
print(txt.find("na"))     # 2 (first position)
print(txt.rfind("na"))    # 10 (last position)
print(txt.index("na"))    # 2 (like find, but error if not found)
print(txt.rindex("na"))   # 10 (last position, error if not found)
print(txt.startswith("ba")) # True
print(txt.endswith("na"))   # True

#CHECK STRING PROPERTIES 
txt = "Python3"
print(txt.isalnum())      # True (letters + numbers)
print("Python".isalpha()) # True (only letters)
print("123".isdigit())    # True
print("123".isdecimal())  # True
print("Ⅳ".isnumeric())    # True (Roman numeral counts as numeric)
print("hello".islower())  # True
print("HELLO".isupper())  # True
print("Hello World".istitle()) # True
print("   ".isspace())    # True (only whitespace)
print("abc".isascii())    # True (all ASCII)
print("var_name".isidentifier()) # True (valid Python identifier)
print("Hello!".isprintable())    # True


#SPLITTING AND JOINING
txt = "apple,banana,cherry"
print(txt.split(","))     # ['apple', 'banana', 'cherry']
print(txt.rsplit(",", 1)) # ['apple,banana', 'cherry']
print("Hello\nWorld".splitlines()) # ['Hello', 'World']

words = ["apple", "banana", "cherry"]
print("-".join(words))    # apple-banana-cherry


#REPLACE AND PARTITION 
txt = "I like bananas"
print(txt.replace("bananas", "apples")) # I like apples

txt = "apple-banana-cherry"
print(txt.partition("-"))  # ('apple', '-', 'banana-cherry')
print(txt.rpartition("-")) # ('apple-banana', '-', 'cherry')

#ENCODING 
txt = "hello"
print(txt.encode())       # b'hello' (bytes)

# maketrans + translate
table = str.maketrans("ae", "12")
print("apple".translate(table))  # 1ppl2


#string formatting 
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  