#The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)

#The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3)
print(x)

import math
a = math.cos(30)
b = math.tan(30)
c = math.log(10)
d = pow(2, 3)
e = math.factorial(5)
x = math.sqrt(64)
y = math.ceil(1.4)
z = math.floor(1.4)
print(a)
print(b)
print(c)
print(d)
print(e)
print(x)
print(y) 
print(z) 


#datetime in python

import datetime
x = datetime.datetime.now()
print(x)

datetime_obj = datetime.date.today()
print(datetime_obj)

from datetime import datetime
datetimenow = datetime.now().time()
print(datetimenow)

timenow = datetimenow.strftime("%H : %M: %S")
print(timenow)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import calendar as cal
for i in range(1,13):
    print(cal.month(2026,i))


import calendar
print(calendar.calendar(2026))

import calendar
print(calendar.month(2026, 6))

