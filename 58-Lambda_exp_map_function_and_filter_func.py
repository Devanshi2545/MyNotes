#Lambda expression Maps and filter
#Functions that are used once and cannot be used again
 #say


def square(num):
    return num**2

my_nums=[1,2,3,4,5]
for item in map(square,my_nums):
    print(item)
    
print(list(map(square,my_nums)))

#---------------------------------------------------------
def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]
    
names=['Andy','Eve','charley']
print(list(map(splicer,names)))


#Certainly! In Python, the `map()` function is a built-in function that applies a specified function to all the items in an input iterable (e.g., a list, tuple, or string) and returns an iterator that produces the results. The general syntax of the `map()` function is as follows:


#map(function, iterable, ...)


#`function`: The function to apply to each item in the iterable.
#iterable`: The iterable (e.g., list, tuple, string) whose elements will be processed by the function.

#Here are a few examples to illustrate the usage of the `map()` function:

### Example 1: Doubling numbers in a list

numbers = [1, 2, 3, 4, 5]

# Using map to double each element in the list
doubled_numbers = map(lambda x: x * 2, numbers)

# Converting the result to a list
result_list = list(doubled_numbers)

print(result_list)
# Output: [2, 4, 6, 8, 10]


### Example 2: Converting temperatures from Celsius to Fahrenheit


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_celsius = [0, 10, 20, 30]

# Using map to apply the conversion function to each temperature
temperatures_fahrenheit = map(celsius_to_fahrenheit, temperatures_celsius)

# Converting the result to a list
result_list = list(temperatures_fahrenheit)

print(result_list)
# Output: [32.0, 50.0, 68.0, 86.0]


### Example 3: String length for a list of words


words = ["apple", "banana", "orange", "kiwi"]

# Using map to get the length of each word in the list
word_lengths = map(len, words)

# Converting the result to a list
result_list = list(word_lengths)

print(result_list)
# Output: [5, 6, 6, 4]

#-----------------------------------------
#In each example, the `map()` function is used to apply a specific operation (doubling, temperature conversion, string length) to each element of the input iterable, resulting in a new iterable with the transformed values.
#Absolutely! Let's break it down in simpler terms.

#The `map()` function in Python helps you do something to each item in a group (like a list or a bunch of words). You provide a rule, and it applies that rule to every item in the group, giving you a new bunch of results.

#Here are some examples:

### Example 1: Doubling numbers in a list

#Suppose you have a list of numbers like `[1, 2, 3, 4, 5]`. You want to double each number.


numbers = [1, 2, 3, 4, 5]

# Applying the rule: double each number
doubled_numbers = map(lambda x: x * 2, numbers)

# Result: [2, 4, 6, 8, 10]

### Example 2: Converting temperatures from Celsius to Fahrenheit

#Imagine you have temperatures in Celsius like `[0, 10, 20, 30]`, and you want to convert them to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_celsius = [0, 10, 20, 30]

# Applying the rule: convert each temperature
temperatures_fahrenheit = map(celsius_to_fahrenheit, temperatures_celsius)

# Result: [32.0, 50.0, 68.0, 86.0]


### Example 3: String length for a list of words

#Suppose you have a list of words like `["apple", "banana", "orange", "kiwi"]`. You want to find the length of each word.


words = ["apple", "banana", "orange", "kiwi"]

# Applying the rule: find the length of each word
word_lengths = map(len, words)

# Result: [5, 6, 6, 4]


#In each example, `map()` makes it easy to do the same thing to every item in a group and get a new group of results.


#exapmle 
def check_even(num):
    return num%2==0
my_nums=[1,2,3,4,5,6]

print(list(filter(check_even,my_nums)))


#LAMBDA FUNCTION
#In Python, a lambda expression is a way to create small, anonymous functions. It is a concise way to define a function with a single line of code. Lambda functions are often used for short, simple operations where a full function definition would be overkill.

#The general syntax of a lambda expression is:


#lambda arguments: expression


#`lambda`: Keyword indicating the creation of a lambda function.
#`arguments`: Input parameters for the function.
#`expression`: The operation to be performed on the input parameters.

#Here's a simple example to illustrate the use of a lambda expression:

# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
lambda_add = lambda x, y: x + y

# Using both functions
result_regular = add(2, 3)
result_lambda = lambda_add(2, 3)

print(result_regular)  # Output: 5
print(result_lambda)   # Output: 5

#In this example, the lambda expression `lambda x, y: x + y` is equivalent to the regular function `add(x, y)`. The lambda function takes two arguments (`x` and `y`) and returns their sum.

#Lambda functions are commonly used with functions like `map()`, `filter()`, and `sorted()` where a short, throwaway function is needed. For instance:

numbers = [1, 2, 3, 4, 5]

# Using lambda with map to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Result: [1, 4, 9, 16, 25]


#In this case, the lambda function `lambda x: x ** 2` is used to square each number in the `numbers` list using the `map()` function.
#-------------------------------------------------------------------------------------------------------------------------------------------------


#FILTER
#In Python, the `filter()` function is used to filter elements of an iterable (e.g., a list) based on a specified condition. It takes two arguments: a function and an iterable. The function is applied to each element of the iterable, and only the elements for which the function returns `True` are included in the result.

#The general syntax of the `filter()` function is as follows:


#filter(function, iterable)


#`function`: A function that tests each element of the iterable. If the function returns `True`, the element is included in the result; otherwise, it is excluded.
# `iterable`: The iterable (e.g., list, tuple, string) containing the elements to be filtered.

#Here's an example to illustrate the use of the `filter()` function:


# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get only the even numbers
even_numbers = filter(is_even, numbers)

# Converting the result to a list
result_list = list(even_numbers)

print(result_list)
# Output: [2, 4, 6, 8, 10]


#In this example, the `is_even` function is used as the filtering condition. The `filter()` function applies this condition to each element in the `numbers` list, and only the even numbers are included in the result.

#You can also use lambda expressions with `filter()` for a more concise one-liner:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda expression to get only the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Converting the result to a list
result_list = list(even_numbers)

print(result_list)
# Output: [2, 4, 6, 8, 10]


#This example achieves the same result as the previous one but uses a lambda function for brevity.