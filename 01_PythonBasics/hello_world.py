def greet_the_world():
    return "Hello, world!"

if __name__=="__main__":
    greetings = greet_the_world()
    print(greetings)

#Practice
import this 
 
a = "I like"
b = "banana"
c = a+" "+b

#Classes
type(True)
type
type(a)
type(None)
type(print())
print(type(a))

from datetime import datetime
o5 = datetime(2021,1,23,18)
print(o5)
type(o5)

o4 = {'a':[2,3],'b':3}
print(o4["a"])

#Attribute and method
c.replace('banana','apple')
c.upper().lower().split(" ").upper()
c.upper().lower().split(" ")

dir(c) 

#functions
def add(x,y):
    return x+y
add(2,3)
add("I","love")

#Identations TAB
for i in range(100):
    print(i)
    if i<50:
        print("fuck")
    else:
        print("not fuck")
# \ IS USED FOR SPACING 
if 1900 < year < 2100 and 1 <= month <= 12 \ 
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:
   pass

import keyword
print(f"{keyword.kwlist} \n\n {dir(__builtins__)}") #DO NOT USE THESE NAMES FOR VARIABLES

#Data types
integer = 2
print('Integer: ',integer, type(integer))

float = 1.32
print('Float: ',float, type(float))

integer + float

7 % 2 
15 // -4

if 0:
    print('ok')
elif False:
    print('also ok')
elif True:
    print('not ok')
    
print(f'I can tell the truth more times: {True + True} times to be precise') #f string
txt_var = 'This is a text variable'
print(f"I have myself and I print some value {txt_var}")
'   IES FSV UK    '.strip() #remove white spaces at the beginning and the end
'   IES FSV UK    '.replace(" ","*") #remove white spaces
a = chr(123123) #emojis
print(a)

#LISTS
tmp = list('abcde')
tmp.append("a")
tmp
len(tmp)
tmp[7]
for i in tmp:
    print(i)
colors = ['red', 'blue', 'green', 'black', 'white']
type(colors)
print(f"{colors[2]} {colors[-1]} {colors[-2]}")
print(colors[2:])
print(colors[-2:])
print(colors[::2]) #take every second element 
colors.append('yellow') 
colors.extend(['pink', 'purple']) # extend colors, in-place

#DICTIONARIES
tel = {'emmanuelle': 5752, 'sebastian': 5578}
print(tel)
tel['francis'] = 5915
print(tel.keys())
print(tel.values())
'francis' in tel
for key, value in tel.items():
    print(f"under key {key} is value {value}")

#TUPLES
l = list('abcd')
t = tuple(l) # or declare as ('a', 'b', 'c', 'd')
coord = (50.082,14.431)
print(l, t, coord )
l[0]='z'
t[0]='z'

if 2**2 == 4:
    print('Obviously!')

#Control flows
for i in range(4):
    print(f"Running iteration with index {i}")    
for word in ('cool', 'powerful', 'readable'):
    print(f'Python is {word} ')
for idx, word in enumerate(('cool', 'powerful', 'readable')):
    print(f'Python is {word} - run {idx}')

a = []
b = [1,2,3]

if a:
    print('got a')
else:
    print('empty array')
if b:
    print('got b')

global a
for i in range(5,-5,-1):
    print(5/i)

first = input("First: ")
second = input("Second: ")2
print(f"Sum is {float(first) + float(second)}")

x = "I"

weight = input("Weight:" )

measurement = input("Kg or Lbs: ")k
if measurement == "L" or measurement == "l":
    print(f"Weight in Kg: {float(weight)*2.2}")
elif measurement == "K" or measurement == "k":
    print(f"Weight in Lbs: {float(weight)/0.45 }")

i = 1
while i <= 10000:
    print(i)
    i = i+1

#Lecture 2
list("hello")

squares = [x**2 for x in range(10)] # WE CAN DO IT IN ONE LINE
squares

matrix = [[1,2,3],[1,2,3], [1,2,3]]
matrix

list11 = list('ht')
list11.index("t")
for i in list11:
    i == list11

import itertools
import random
arr = [1, 2, 3, 4, 5,6,7,8]
combinations = []
for _ in range(len(arr)):
    combinations.extend(list(itertools.combinations(random.sample(arr, 4), 4)))
print(combinations)

all_comb = list(itertools.combinations(arr, 4))
print(all_comb)
len(all_comb)
