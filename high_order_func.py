from functools import reduce

# fiter function

my_list = [1,4,5,6,9,13,19,21]
# ods = [i for i in my_list if i%2 != 0] # Usando list comprehension
ods = list(filter(lambda x: x%2 != 0, my_list)) # Usando filter
print(ods)


# map function

my_list2 = [1,2,3,4,5]
# squares = [i**2 for i in my_list2] # Usando list comprehension
squares = list(map(lambda x: x**2, my_list2)) # Usando map
print(squares)


# reduce function

my_list3 = [2,2,2,2,2]
# all_multiplied = 1
# for i in my_list3:
#     all_multiplied = all_multiplied * i # Mediante el ciclo for
all_multiplied = reduce(lambda a, b: a * b, my_list3)
print(all_multiplied)