# code to print version of python
from math import sqrt
import sys
print("Python Version: ",sys.version)

#code to print date and time
import datetime
now = datetime.datetime.now()
print("Current date and time is : ",now.strftime("%Y-%m-%d %H %M %S"))

#function that accepts input of radius
radius = input("Enter radius of circle: ")
radius_int = int(radius)
Area = sqrt(2.0)*radius_int*radius_int
print("Area of circle: ",Area)

#program that accepts user name as input

firstName = input("Enter your First Name: ")
lastName = input("Enter your last Name:")
print("Your name is  ",lastName,firstName)

#Enter number print in a list and tuple\
numbers = input("Enter 3 numbers:")
list = numbers.split(",")#splits by a comma
tuple = tuple(numbers)
print("List:",list)
print("Tuple:",tuple)
#print file exitension

ext = input("Filename with extension:")
ext_print = ext.split(".")
print(ext_print[1])

#print and first from a list
color_list = ["Red","Green","White" ,"Black"]
print("First Colour:",color_list[0],"Last Colour:",color_list[3])

#print numbers from a list
exam_st_date = (11, 12, 2014)
print("%d/%d/%d"%(exam_st_date[0],exam_st_date[1],exam_st_date[2]))#

#accept integers
num = input("Enter integer:")
n = int(num)
total = n + n*n + n*n*n
print(total)

#calendar module
#using calendar module
import calendar
i = int(input("Enter year:"))
y = int(input("Enter Month:"))
print(calendar.month(i,y))

#length of days
import datetime
f_days = datetime.date(2014,7,23)
l_days = datetime.date(2014,8,4)
diff = l_days - f_days
print(diff.days)

#length of string
string = input("Enter name:")
print("Length of string is ",len(string))
