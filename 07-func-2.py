# Variable length arguments
def sum_all(*args):
  print(args)
  total = 0
  for value in args:
    total = total + value
  return (sum(args), total)
  # return sum(args)
  

print(sum_all(1,2,3,4,5))
print(sum_all(2,4,5))
print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6,7,8,9,2,4,54,66))

sm, total = sum_all(1,2,3) 
print(sm, total)

result = sum_all(1,2,3)
print(result)



# kwargs
def print_kv(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f"{key} : {value}")

print_kv(name="Python", lang_type="High Level")
print_kv(first_name="Amit", percent="80", grade="A")


# Assignment -> multiply all arguments
def mul(*args):
    result = 1
    for number in args:
        result *= number
    return result    

print(mul(2,3))
print(mul(2,3,4,5))




