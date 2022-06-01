import random

# def random_list_generator(n):
#     result = []
#     for _ in range(n):
#         result.append(random.randint(1, 10))
#     return result
# print(random_list_generator(4))


def random_list_generator(n, my_randint):
    result = []
    for _ in range(n):
        result.append(my_randint(1, 10))
    return result

# print(random_list_generator(4, random.randint))