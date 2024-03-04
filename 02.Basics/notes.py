#Lists
my_list = range(5)
print(my_list)
len(my_list)
reversed_list = my_list[::-1]
reversed_list

list1 = [x**5 for x in range(5)]
list1

sum(my_list)
min(my_list)

coordinates = [(x, y) for x in range(3) for y in range(3)]
coordinates

for i in coordinates:
    print(type(i))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
transposed    

#Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('a', 0)  # Get value with a default
value
popped = my_dict.pop('b', 0)  # Remove item, default if not found
popped
my_dict
my_dict.update({'d': 4, 'e': 5})  # Add multiple key-value pairs
my_dict

#defaultdic
from collections import defaultdict #import library, top of the script!!

fruits = ['apple', 'banana', 'cherry', 'apple', 'cherry'] #could how many of each we have
fruit_counts = defaultdict(int)
for fruit in fruits:
    fruit_counts[fruit] += 1
fruit_counts

#FUNCTIONS
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print(f"Something is happening after the function '{func.__name__}' is called.")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()

def converter(romnum):
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_value = 0
    
    for char in romnum:
        value = roman_numbers[char]
        if value > prev_value:
            result += value - 2*prev_value
        else:
            result += value
        prev_value = value
        
    return result

roman_to_int("XM")