#if: use when you want to execute code only when a condition is true 
age = 20
if age >= 18:
    print("You can vote")

#if-else: use when there are 2 choices 
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#if-elif-else: when multiple choices 
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

#nested if
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")


#multiple if: all condition are checked 
num = 15

if num > 0:
    print("Positive")

if num % 3 == 0:
    print("Divisible by 3")

if num % 5 == 0:
    print("Divisible by 5")


#match 
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

