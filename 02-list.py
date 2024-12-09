# Example of creating a list 
# List is mutable 
fruits = ["apple", "orange", "chickoo","grapes"]

everything = ["apple", "orange", 10, 20, True, False]

print(fruits) 
print(everything)

print(fruits[0])
print(everything[3])

# last element
print(fruits[3])
print(everything[5])

# negative indexing
print(fruits[-1])
print(everything[-1])

# second last element
print(fruits[-2])
print(everything[-2])

# Slice 
nums = [0,1,2,3,4,5,6,7,8,9,10]

#nums[start:end:step]    # start -> index to begin, end-> last index excluding end, step->Skip

print(nums[3:])
print(nums[0:10:3])

print(f"{len(nums)=}")

# Operatons on array
# insert, append, remove, edit

nums.append(11)

print(nums)

# insert at index
nums.insert(1, 99) 
print(nums)

# remove
last = nums.pop()
print(f"{last=}")

print(f"{nums=}")

ele = nums.pop(3)
print(f"{ele=}")
print(f"{nums=}")

# remove element directly
print(nums.remove(99))
print(nums)

# nums.remove(1000) # error as element is not present

# edit
nums[9] = "hello" 
print(nums)

nums.append(6) 

print(nums) 

# nums.remove(6)  # remove first occurence of value 6

print(nums)
# finding elements
# using index
idx = nums.index(6) 
print(f"{idx=}")

# count
print(f"{nums.count(6)=}")
print(f"{nums.count(7)=}")

# remove
nums.remove("hello")
print(nums)

nums.append(13)
nums.append(22) 
nums.append(12)

print(nums)
# sort -> by default asc, mutable operation
nums.sort() 
print(nums)

nums.sort(reverse=True)
print(nums)


nums.append("hello")
print(nums)
# nums.sort()   # error because heterogenous elements in list 

# convert all elements to strings for sorting 
nums.sort(key=str)
print(nums)



# Useful functions
print(type(1))
print(type(nums))
print(type(True))
print(type(1.2))



# Nesting list 
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

print(nested_list[0])
print(nested_list[1])
print(nested_list[1][0])

print(nested_list[:2])


# List comprehensiion
print(nums)

# Useful function
# range()

print(range(5))

elems = [x for x in range(5)]
print(elems)

squared = [x**2 for x in elems]
print(f"{squared=}")


something = [n for n in nums]
print(something)

nested_1 = [n for n in nested_list]
print(nested_1)

# flatten
flattened = [item for sublist in nested_list for item in sublist]
print(f"{flattened=}")

# Logic 
# flattened = [] 
# for sublist in nested_list:  # outer loop 
#   for item in sublist:  # inner 
#     flattened.append(item)


# [expression for outer_loop for inner_loop]






























