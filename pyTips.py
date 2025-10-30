# Showing python tips

# Create a class to handle colours in terminal output
# This simply creates a new object that contains colour codes as attributes and a fubction to apply them to text
class Colours:
    def __init__(self):
        # Regular colors
        self.red = '\033[91m'
        self.green = '\033[92m'
        self.blue = '\033[94m'
        self.yellow = '\033[93m'
        self.magenta = '\033[95m'
        self.cyan = '\033[96m'
        self.white = '\033[97m'
        self.reset = '\033[0m'
    
    def colourize(self, text, colour):
        """Add colour to text and handle reset automatically"""
        colour_code = getattr(self, colour.lower(), '')
        return f"{colour_code}{text}{self.reset}"

# Create an instance of Colours
colours = Colours()

# Pass-by-object-reference
#
# Integers, strings, and tuples () are immutable; lists [], dictionaries {key: value, key: value} or dict(), and sets {item, another, third } or set() are mutable.
# So, integers, strings, and tuples behave like pass-by-value, while lists, dictionaries, and sets behave like pass-by-reference.
#
# Immutable int, float, str, tuple() -> Changes create a new object
# Mutable list [], dict {k:v}, set {a,b,c} -> Changes modify the original object
#
# An integer is immutable so the modification creates a new object 
print(colours.colourize("Passing variables","red"))
print(colours.colourize("Modify","blue"))

def modify(num):
    num += 1
    print("Inside:", num)

x = 5
modify(x)
print("Outside:", x) # x remains 5
print()

# A list is mutable so the modification affects the original object
print(colours.colourize("Add item","blue"))
def add_item(items, value):
    items.append(value)
    return items

my_list = [1, 2, 3]
add_item(my_list, 4)
print(my_list)  # [1, 2, 3, 4] - modified in place wihtout assignment in the row above that calls add_item()
print()

# Mutable default arguments are evaluated once at function definition
print(colours.colourize("Add to list","blue"))
def add_to_list(value, items=[]):
    items.append(value)
    return items

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] - not a fresh list!
print()

# Argument handling
# In this example 'a' is the first positional argument
# *args collects additional positional arguments as a tuple
# **kwargs collects keyword arguments as a dictionary
#
# Must be in this order: positional, *args, **kwargs although you can omit any of them
#
print(colours.colourize("Argument handling","red"))
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, x=4, y=5)
print()

# 'is' vs '=='
print(colours.colourize("Comparison operators 'is' vs '=='","red"))
a = [1, 2]
b = [1, 2]
print(a == b) # True (values are equal)
print(a is b) # False (different object)
print()

# Inner functions
#
print(colours.colourize("Functions","red"))
print(colours.colourize("Inner functions","blue"))
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

parent()
print()

#
# Returning functions
print(colours.colourize("Returning functions","blue"))
def parental(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child

first = parental(1)
second = parental(2)

print(first())  # Hi, I'm Elias
print(second()) # Call me Ester 
print()

# Decorators
print(colours.colourize("Decorators","blue"))
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    print(f"Hello, {name}")

greet("Python")
print()

# Types
print(colours.colourize("Types","red"))
print(colours.colourize("Type investigation","blue"))

print(type(42)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("Hello")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>
print(isinstance(3.14, float)) # True
print(issubclass(int, object)) # True - everything inherits from object
print()

print(colours.colourize("Type conversion","blue"))
print(int("42")) # 42
print(float("3.14")) # 3.14
print(str(42)) # "42"
print(bool(1)) # True
print(list("abc")) # ["a", "b", "c"]
print()

# Variables
print(colours.colourize("Variables","red"))
print(colours.colourize("Variable assignment","blue"))
name = "Leo" # String
counter = 7 # Integer
height = 5.6 # Float
is_cat = True # Boolean
flaws = None # None type
print()

print(colours.colourize("Augmented assignment","blue"))
counter += 1
print(counter)
numbers = [1,2,3]
numbers += [4, 5]
print(numbers)
print()

# Variables
print(colours.colourize("Strings","red"))
print(colours.colourize("Creating strings","blue"))

single = 'Hello'
double = "World"
multi = """Multiple
line string"""

print(single)
print(double)
print(multi)
print()

print(colours.colourize("String operations","blue"))
greeting = "me" + "ow!" # "meow!"
repeat = "Meow!" * 3 # "Meow!Meow!Meow!"
length = len("Python") # 6

print(greeting)
print(repeat)
print(length)
print()

print(colours.colourize("String methods","blue"))
print("Upper:", "a".upper()) # "A"
print("Lower:", "A".lower()) # "a"
print("Strip:", " a ".strip()) # "a"
print("Replace:", "abc".replace("bc", "ha")) # "aha"
print("Split:", "a b".split()) # ["a", "b"]
print("Join:", "-".join(["a", "b"])) # "a-b"
print()

print(colours.colourize("String indexing and slicing","blue"))
print("text = Python")
text = "Python"
print("Index 0", text[0]) # "P" (first)
print("Index -1", text[-1]) # "n" (last)
print("Slice 1:4 (start at 1 upto but not including 4)", text[1:4]) # "yth" (slice)
print("Slice :3 (upto but not including 3)",text[:3]) # "Pyt" (from start)
print("Slice 1: (from 1 to the end)",text[1:]) # "ython" (to end)
print("Slice ::2 (every second)", text[::2]) # "Pto" (every 2nd)
print("Slice ::-1 (reverse)", text[::-1]) # "nohtyP" (reverse)
print()


print(colours.colourize("String formatting","blue"))
# f-strings
print("name = Aubrey, age = 2")

name = "Aubrey"
age = 2
print(f"Hello, {name}!") # "Hello, Aubrey!"
print(f"{name} is {age} years old") # "Aubrey is 2 years old"
print(f"Debug: {age=}") # "Debug: age=2"
print()

# Format method
template = "Hello, {name}! You're {age}."
formatted = template.format(name="Aubrey", age=2) # "Hello, Aubrey! You're 2."
print(formatted)
print()

print(colours.colourize("Raw strings","blue"))
# Normal string with an escaped tab
print("This is:\tCool.") # "This is: Cool."
# Raw string with escape sequences
print(r"This is:\tCool.") # "This is:\tCool."
print()

print(colours.colourize("Numbers & Maths","red"))
print(colours.colourize("Basic arithmetic","blue"))
print(10 + 3) # 13
print(10 - 3) # 7
print(10 * 3) # 30
print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3
print(10 % 3) # 1
print(2 ** 3) # 8
print()

print(colours.colourize("Useful Functions","blue"))
print(abs(-5)) # 5
print(round(3.7)) # 4
print(round(3.14159, 2)) # 3.14
print(min(3, 1, 2)) # 1
print(max(3, 1, 2)) # 3
print(sum([1, 2, 3])) # 6

print(colours.colourize("Conditionals","red"))
print(colours.colourize("If-Elif-Else","blue"))
age = 13
if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"
print(category)
print()

print(colours.colourize("Comparison Operators","blue"))
print("x, y = 2, 3")
x = 2
y = 3
print()

print("x == y", x == y) # Equal to
print("x != y", x != y) # Not equal to
print("x < y", x < y) # Less than
print("x <= y", x <= y) # Less than or equal
print("x > y", x > y) # Greater than
print("x >= y", x >= y) # Greater than or equal
print()

print(colours.colourize("Logical Operators","blue"))
age, has_car = 19, True
if age >= 18 and has_car:
    print("Roadtrip!")

is_weekend, is_holiday = 0,1
if is_weekend or is_holiday:
    print("No work today.")
is_raining = False
if not is_raining:
    print("You can go outside.")
print()

print(colours.colourize("Loops","red"))
print(colours.colourize("For Loops","blue"))

# Loop through range
for i in range(5): # 0, 1, 2, 3, 4
    print(i)
# Loop through collection
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)
# With enumerate for index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

print()
print(colours.colourize("While Loops","blue"))

while True:
    #user_input = input("Enter 'quit' to exit: ")
    user_input = "quit" # Uncomment the line above and comment this to see it in action
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

print()
print(colours.colourize("Loop Control","blue"))

for i in range(10):
    if i == 3:
        continue # Skip this iteration
    if i == 7:
        break # Exit loop
    print(i)
print()

print(colours.colourize("Functions","red"))
print(colours.colourize("Defining Functions","blue"))
print("def func()")
print("def func(param)")
print("def func(param, default=2)")
def greet():
    return "Hello!"
def greet_person(name):
    return f"Hello, {name}!"
def add(x, y=10): # Default parameter
    return x + y

print(colours.colourize("Calling Functions","blue"))
print(greet()) # "Hello!"
print(greet_person("Bartosz")) # "Hello, Bartosz"
print(add(5, 3)) # 8
print(add(7)) # 17
print()

print(colours.colourize("Return values","blue"))
def get_min_max(numbers):
    return min(numbers), max(numbers)
minimum, maximum = get_min_max([1, 5, 3])
print("Min:", minimum, "Max:", maximum)
print()

print(colours.colourize("Useful built-in functions","blue"))
print("callable(x):")
print(callable(x))
print() # Checks if an object can be called as a function
print("dir(): Names in the current local scope")
print(dir())
print() # Lists attributes and methods
print("dir(x): Valid attributes and methods for the object x")
print(dir(x))
print()
print("globals(): A dictionary of the current global symbol table")
print(globals()) # Get a dictionary of the current global symbol table
print()
print("locals(): A dictionary of the current local symbol table")
print(locals()) # Get a dictionary of the current local symbol table
print()
print(f"Hash of 181: {hash(181)}") # Hashing an int
print(f"Hash of 181.23: {hash(181.23)}")# Hashing a float
print(f"Hash of 'Python': {hash('Python')}") # Hashing a string
vowels = ('a', 'e', 'i', 'o', 'u')
print(f"Hash of vowels tuple: {hash(vowels)}") # Hashing an immutable tuple
print()

print("a = [1, 2, 3]")
a = [1, 2, 3]
print("b = a")
b = a  # b refers to the same list object as a
print("c = [1, 2, 3]")
c = [1, 2, 3] # c refers to a new list object, even though its value is the same

print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print(f"ID of c: {id(c)}")
print()

# Using repr() on built-in types
print("my_list = [1, 2, 'hello']")
my_list = [1, 2, 'hello']
print(f"repr(my_list): {repr(my_list)}")
print()

print("my_string = \"Hello\nWorld\"")
my_string = "Hello\nWorld"
print(f"repr(my_string): {repr(my_string)}")
print()

# Using repr() on a custom class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
print("my_product = Product(\"Laptop\", 1200.00)")
my_product = Product("Laptop", 1200.00)
print(f"repr(my_product): {repr(my_product)}")
print()

print(colours.colourize("Lambda functions","blue"))
print("square = lambda x: x**2")
square = lambda x: x**2
print("result = square(5)")
result = square(5) # 25
print("Result:",result)
print()
# With map and filter
print("numbers = [1, 2, 3, 4]")
numbers = [1, 2, 3, 4]
print("squared = list(map(lambda x: x**2, numbers))")
squared = list(map(lambda x: x**2, numbers))
print(squared)

print("evens = list(filter(lambda x: x % 2 == 0, numbers))")
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
print()

print(colours.colourize("Classes","red"))
print(colours.colourize("Defining Classes","blue"))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"
# Create instance
my_dog = Dog("Frieda", 3)
print(my_dog.bark()) # Frieda says Woof!

print()
print(colours.colourize("Class Attributes & Methods","blue"))

class Cat:
    species = "Felis catus" # Class attribute
    def __init__(self, name):
        self.name = name # Instance attribute
    def speak(self):
        return f"{self.name} says Meow!"
   
    @classmethod
    def create_kitten(cls, name):
        return cls(f"Baby {name}")
    
# Accessing the class attribute
print(f"Species: {Cat.species}") # Felis catus
print()
# Using the __init__ method
bob = Cat("Bob")
print(bob.speak())
# Using the classmethod as an alternative constructor
kitty = Cat.create_kitten("Dave")
print(kitty.speak()) # Baby dave says Meow!
print()

print(colours.colourize("Inheritance","blue"))
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        # We don't need any code here, the classes that inherit will implement their own speak()
        # pass is valid syntax placeholder code that does nothing
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"
    
rex = Dog("Rex")
print(rex.speak())
print(bob.speak())
print()

print(colours.colourize("Exceptions","red"))
print(colours.colourize("Try-Except","blue"))

try:
    # number = int(input("Enter a number: "))
    number = 7
    result = 22 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Calculation attempted")

print()
print(colours.colourize("Common Exceptions","blue"))

print("ValueError # Invalid value")
print("TypeError # Wrong type")
print("IndexError # List index out of range")
print("KeyError # Dict key not found")
print("FileNotFoundError # File doesn't exist")
print()

print(colours.colourize("Collections","red"))
print(colours.colourize("Lists (mutable)","blue"))
print()

# Creating lists
print("empty = []")
empty = []
print("nums = [5]")
nums = [5]
print("mixed = [1, \"two\", 3.0, True]")
mixed = [1, "two", 3.0, True]
print()

# List methods
print("nums.append(\"x\") # Add to end")
nums.append("x") # Add to end
print("nums.insert(0, \"y\") # Insert at index 0")
nums.insert(0, "y") # Insert at index 0
print("nums.extend([\"z\", 5]) # Extend with iterable")
nums.extend(["z", 5]) # Extend with iterable
print("nums.remove(\"x\") # Remove first \"x\"")
nums.remove("x") # Remove first "x"
print("last = nums.pop() # Pop returns last element")
last = nums.pop() # Pop returns last element
print()

# List indexing and checks
print("fruits = [\"banana\", \"apple\", \"orange\"]")
fruits = ["banana", "apple", "orange"]

print("fruits[0]:", fruits[0]) # banana
print("fruits[-1]:", fruits[-1]) # orange

is_it_there = lambda x: x in fruits # True
print("Is apple in fruits?", is_it_there("apple"))
print("Is cherry in fruits?", is_it_there("cherry"))

print("len(fruits):", len(fruits)) # 3
print()

print(colours.colourize("Tuples (immutable)","blue"))
print()

# Creating tuples
print("point = (3, 4)")
point = (3, 4)

print("single = (1,) # Note the comma!")
single = (1,) # Note the comma!

print("empty = ()")
empty = ()

# Basic tuple unpacking
print("x, y = point")
x, y = point
print("x:", x)  # 3
print("y:", y) # 4

# Extended unpacking
print("first, *rest = (1, 2, 3, 4)")
first, *rest = (1, 2, 3, 4)
print("first:", first) # 1
print("rest", rest, "# Note the return is a list") # [2, 3, 4]
rest.append(5)
print("rest.append(5): ", rest)
print()
