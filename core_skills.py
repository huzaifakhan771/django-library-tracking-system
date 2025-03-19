import random
rand_list = [random.randint(1,20) for i in range(1,20)]

list_comprehension_below_10 = [num for num in rand_list if num <10]

list_comprehension_below_10 = list(filter(lambda num: num<10,rand_list))


print(rand_list)
print(list_comprehension_below_10)
print(list_comprehension_below_10)