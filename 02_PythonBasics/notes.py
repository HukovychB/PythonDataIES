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

def converter(number):
        roman_numbers = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        num = 0
        prev_num = 0
        for char in number:
            value=roman_numbers[char]
            if value > prev_num:
                num+=roman_numbers[char]- 2*prev_num
            else:
                num+=roman_numbers[char]
            prev_num=value
        return(num)
converter("IIV")

def twoSum(nums, target):
    for i in range(len(nums)):  # Use range(len(nums)) to iterate over indices
        for j in range(i+1, len(nums)):  # Start inner loop from i+1 to avoid duplicate pairs
            if nums[i] + nums[j] == target:
                return [i, j]
twoSum(nums=[3,2,4],target=6)                        
str(12)
for i in str(12):
    print(i)
list11.index("t")
for i in list11:
    i == list11[]

my_list1 = [0,1,2,3]
my_list2 = [0,1,2,3]
my_list1 == my_list2
def isPalindrome(x):
        num = list(str(x))
        reversed_num = list(str(x))[::-1]
        return(num == reversed_num)
isPalindrome(12222221)