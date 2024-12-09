# print("Hello, World!")
# print("hello", "123", "apple")

# # String variable
# name = "Python" 
# nature = 'Python is cool'

# print(name, nature)

# # variables is mutable (mostly)

# name = "AI/ML"
# print(name) 



# age = 45 # integer
# sales = 100.5   # decimal/float

# success = True  # Boolean
# failure = False 

# print(age, sales, success, failure)

# success_is_not_that_greate_45_ = 10

# # 123_valid = 10

# _something = 10

name = "Tom"
age = 30 

print(name, age) 


print(name + " is " + str(age) + " years old")
print(f"{name} is {age} years old") 

print(f"{name=}")  # debugging

salary = 100.503343
print(f"{salary:.2f}") # decimal precision

from datetime import datetime  
now = datetime.now()

print(now) 
print(f"Current time: {now:%H:%M:%S}")

# Alignment
text = "Hello" 

print(f"{text:*>20}")  # Right align with '*'

print(f"{text:*<20}")  # hopefully left align with '*'


filename = "data"
ext = "csv"

# print output: data.csv
print(filename + "." +  ext) 
print(f'{filename}.{ext}')


# Profit: 123456.79
profit = 123456.789 
print(f"Profit: ${profit:,.2f}")
























































