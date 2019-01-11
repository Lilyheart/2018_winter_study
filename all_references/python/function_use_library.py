import builtins
from functools import reduce
####
# Misc
####

# printing quirks
print("C:\the\name")  # error!
print("C:\\the\\name")  # escape the \
print(r"C:\the\name")  # or set as raw with r before the string

print("""Multi
Line""")  # includes line return
print("""Multi\
Line""")  # the \ means the line return is ignored

print("weird" " concat")  # literals only - not variables

name, age, height = "John Doe", 21, 5.75
generic_names = ["John Doe", "Jane Doe"]
print("%s is %d years old and is %.2f feet tall" % (name, age, height))
print("Names %s" % generic_names)
print("John's age in hex %x/%X" % age)

print(name[0:10:2])  # start, stop, skip - extended slice syntax
print(name[::-1])  # string reverse
print(name.startswith("A"))
print(name.endswith("A"))
print(name.split(" "))

# Exponentation (2^4)
print(2 ** 4)

# variables
height = 1.79  # meters
weight = 74.2  # kg

bmi = weight / (height ** 2)
print(bmi)

type(bmi)

round(1.68, 1)  # 1.7
round(1.68, 1)  # 2
help(round)

# tuples
even_nums = (2, 4, 6)
print(type(even_nums))
print(even_nums)
x, y, z = even_nums
x = even_nums[0]

# comparison - Not has higher prio than and/or
x = 13
x > 5 and x < 18
x < 5 or x > 10
not(x < 5)

y = [1, 2, 3]
z = [1, 2, 3]

print(y == z)
print(y is z)

# loops
z = 6
if z % 2 == 0:
    print("checking " + str(z))
    print("z is even")
elif z % 3 == 0:  # never reached if also even
    print("z is divisible by 3")
else:
    print("z is odd")

# while loops
y = 50
print(str(y))
while y > 1:
    y = y / 4
    print(str(y))
else:
    print("Done!")

# break - exit for or while - skips else
# continue - break current loop

# for loops - iteration
height_list = [1.73, 1.68, 1.71, 1.89]
for height in height_list:
    print(height)
else:
    print("Done!")

for index, height in enumerate(height_list):
    print("index " + str(index) + ": " + str(height))

for index, height in enumerate(height_list, start=1):
    print("index " + str(index) + ": " + str(height))

for letter in "family":
    print(letter.capitalize())

for x in range(10):  # 0 through 9 for 10 iterations
    print(x)

# py2 range creates list up front, xrange creates generator
# py3 range behaves like xrange

# iterable - object associated with iter() method
# iterator - associated next() method

my_iterator = iter("Da")
print(*my_iterator)  # prints entire iterator using "splat"

my_iterator = iter("Da")
print(next(my_iterator))  # "D"
print(next(my_iterator))  # "a"
print(next(my_iterator))  # ERROR: StopIteration

print(sum(iter(height_list)))

height_names = ["sam", "sally", "mom", "dad"]
family_type_zip = zip(height_names, height_list)  # iterable
family_type_list = list(family_type_zip)

"sam" in height_names  # check in iterable

print(*family_type_zip)

unzip_name, unzip_height = zip(*family_type_zip)

family_type_dict = dict(family_type_zip)

# map
result = map(lambda height: height ** 2, height_list)
print(list(result))

# filter
result = filter(lambda height: height > 1.72, height_list)
print(list(result))

# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
# from functools import reduce
result = reduce(lambda height_prod, height: height_prod * height, height_list)
print(result)

# builtins
# import builtins
dir(builtins)
