''' print("Hello World")
indian = ["samosa","deel","egg"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]
print("Enter your first name: ")
dish = input("Enter your dish: ")
if  dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("We don't have your finish")



exp = [30,20,40,20,70,90,20,10]
val = range(1,9)
total = 0
#use for loop,with range
for i in range(len(exp)):
    print("Month: ",(i+1),"Expense: ",exp[i])
    total = total + exp[i]
print(total)

for i in range(1,6):
    if i%2 != 0:
        print(i*i)
    else:
        continue

#continue will skip an elemwnt in a list
#while loop,takes only one condition to bwe satisfied to be true
i = 1
while i<=5:
    print(i*2)
    i = i+1



#functions use def to define a function call it above
def calculate_total_exp(expenses):
    total = 0
    for item in expenses:
        total = total + item
    return total

tom_exp = [20,50,60]
joe_exp = [30,50,60]

tom_total = calculate_total_exp(tom_exp)
joe_total = calculate_total_exp(joe_exp)

print("Tom total expenses: ",tom_total)
print("Joe total expenses: ",joe_total)

def sum(a,b):
    total_sum = a+b
    return total_sum
    
print(sum(2,3))

#range and while
for x in range(10,40,5):
    print(x)#ranges from zero to nine looping through
#while loop loops as long as a condition is true

x = 5

while x <10:
    print(x)
    x+=1 #breaks the loop


#comments and break
magicNumber =26
for n in range(101):
    if n is magicNumber:
        print(n,"magic number found")
        break #the  loop should stop
    else:
        print(n)
    
#to print multiple of 4
for n in range(1,101):
    if n % 4 == 0:
        print(n,'is a multiple of 4')
    else:
        pass

#continue
numbersTaken = [2,3,4,34,15]

for n in range(1,20):
    if n in numbersTaken:
        continue
    print("This number",n," is available")


#keyword arguements

def dumb_sentence(name='Bucky',action='ate',item='tuna'):
    print(name,action,item)


dumb_sentence('Sally','farts','gently')
dumb_sentence(item='OSHI')

#flexible number of arguments
def add_numbers(*args):#use * for any amount of arguement
    total = 0
    for a in args:
        total += a 
    print(total)

add_numbers(3)
add_numbers(3,4,5)

#unpacking argumets
def health_calc(age,apples_ate,cigs):
    answer = (100*age) -(apples_ate*3.5) - cigs
    print(answer)

bucks_date = [1,2,3]

health_calc(*bucks_date)#takes the list and upacks it one at a time


# a set use curly braces,can't have duplicates
groceries = {'cereal','milk','cheese','cheese','mouthwash'}
print(groceries)

if milk in groceries:
    print("You already have milk")
else:
    print("Oh yh  you need milk")

#dictionary,cotaons keys and values
classmates = {'Tony':'idiot',
        'emma': 'fool',
        'idiot':'tony'}

#to use a loop
for k,v in classmates.items():
    print(k+v)

#Modules 
import newfile
newfile.fish()

import random

a = random.randrange(1,1000)#generates random number from range(1,1000)
print(a)


#download an image from the web
import random
import urllib.request#helps get data from website

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpeg"#str() cpnverts number from string
    urllib.request.urlretrieve(url,full_name)#takes two arguements,the url and name you want to store it in
download_web_image("https://images.unsplash.com/photo-1485550409059-9afb054cada4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=401&q=80")'''

#read and write files
fw = open('sample.txt','w') #this opens a file and writes to it
fw.write("First file with python\n")
fw.write('I like semo\n')
fw.close()
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()