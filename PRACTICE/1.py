#number is negative 0 positive
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#profit and loss using if else
cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No Profit No Loss")


#voting code using if else

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


#show result first class second class anad third class 
num = int(input("Enter percentage: "))
if num >= 80:
    print("First Class")
elif num >= 65:
    print("Second Class")
elif num >= 33:
    print("Third Class")
else:
    print("Fail")

#check vowel or consonant 
ch = input("Enter alphabet: ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonant")

ch = input("Enter alphabet: ")
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#given palindrome or not while loop
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

num = input("Enter number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#check if character is upper case or not using if else

ch = input("Enter alphabet: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
else:
    print("Not Uppercase")

ch = input("Enter alhabet")
if ch.isupper():
    print("Uppercase")
else:
    print("Not Uppercase")


#hcf using loop
n = int(input("Enter first number: "))
num = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(n, num) + 1):
    if n % i == 0 and num % i == 0:
        hcf = i

print("HCF =", hcf)


#lcm
n = int(input("Enter first number: "))
num = int(input("Enter second number: "))

bv = max(n, num)

while True:
    if bv % n == 0 and bv % num == 0:
        print("LCM =", bv)
        break
    bv += 1

#input 3 angle of a triangle and check triangle is valid or not 
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#simple interest
p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

si = (p * r * t) / 10
print("Simple Interest =", si)

#print all natural number from num
n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(i)

#find first and last digit f interger using while loop
num = int(input("Enter number: "))
last = num % 10

while num >= 10:
    num = num // 10

first = num
print("First Digit =", first)
print("Last Digit =", last)

#convert uppercase to lowercase and vice cera using if else
ch = input("Enter character: ")
if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())


ch = input("Enter character: ")
if ch >= 'A' and ch <= 'Z':
    print(chr(ord(ch) + 32))
elif ch >= 'a' and ch <= 'z':
    print(chr(ord(ch) - 32))
else:
    print("Not an alphabet")

