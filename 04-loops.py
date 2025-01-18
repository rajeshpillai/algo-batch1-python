# # For loops
# # Basic

# numbers = [1,2,3,4,5]

# # print(numbers[0])
# # print(numbers[1])

# for number in numbers:
#   print(number)

# # range()
# # for i in range(1001):
# #   print(i)


# # string

# for char in 'hello':
#   print(char)

# # for num in 123:
# #   print(num)

# print(dir('hello'))

# print(type('hello'))


fruits = ['apple', "orange", "jalebi"]

# for fruit in fruits:
#   print(fruit)

# en = enumerate(fruits) 
# print(en)

# for index, fruit in en:
#    print(f"Index {index}: {fruit}")

# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")


# break and continue

# for number in range(10):
#   if number == 5:
#     break
#   print(number)

# for number in range(5):
#   if number == 2:
#     continue
#   print(number)



# WHITE LOOP
# count = 0 
# while count <= 5:
#   print(count)
#   count += 2 # count = count + 1

# count = 5 
# while count > 0:
#   print(count)
#   count -= 1

# Quiz

# while True:
#   response = input("Type 'exit' to quit: ")
#   if response.lower() == 'exit':
#       break 


# Quiz
items = [1,2,3]
while items:
    item = items.pop()
    print(item)







