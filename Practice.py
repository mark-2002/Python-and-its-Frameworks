'''# code to print version of python
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
3

def getdate(a,b):
    import datetime
    f_day = datetime.date(a,d)
    l_day = datetime.date(b)
    date_diff = f_day - l_day
    return print(date_diff.days+'days')
getdate("201")

def factorial(n):
    total = n
    while n > 1:
        total = total *(n - 1)
        n-=1
    return total

number = int(input("Enter your number:"))
print(factorial(number))


def alpha_counter(a):
    upper = 0
    lower = 0
    for i in a:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower += 1
        else:
            pass
        

print(alpha_counter('The quick Brown Fox'))'''

def unique_list(a):
    x = []
    for i in a:
        if i not in x:
            x.append(i)
    return x

print(unique_list([1,2,3,3,3,3,4,5]))
#check a prime number
def prime_checker(a):
    if (a%2 != 0):
        if(a%3 != 0):
            if(a%5 != 0):
                return print("This is a prime nuber")
            elif(a==5):
                return print("This is a prime number")
            else:
                return print("This is a prime number")
        elif(a==3):
            return print("This is a prime number")
        else:
            return print("This is not a prime number")

    elif(a==2):
        return print("This is a prime number")
    else:
        return print("This is not a prime number")

num = input("Enter your number:")
print(prime_checker(int(num)))

#check an even number
def even_checker(a):
    x = []
    for e in a:
        if(e%2 == 0):
            x.append(e)
        else:
            pass
    return x
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_checker(list))

#check a perfect number
def perfect_number(x):
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum += i
    if sum == x:
        return print("This is a perfect number")


num2 = input("Enter your number:")
print(perfect_number(int(num2)))

#palindrome code
def palindrome(a):
    x = [] 
    n = len(a) - 1
    i = 0
    while i < n:
        x.append(a[n-i])
        i +=1
    return print("Your Palindrome is:",x)

string = input("Enter your string:")
print(palindrome(string))









