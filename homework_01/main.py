"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [x ** 2 for x in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if (num < 2):
        return False

    prime_flag = True
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            prime_flag = False
            break
    return prime_flag

def filter_numbers(l, param):
    if (param == ODD):
        return list(filter(lambda x: x % 2 != 0, l))
    elif (param == EVEN):
        return list(filter(lambda x: x % 2 == 0, l))
    elif (param == PRIME):
        return list(filter(lambda x: is_prime(x), l))
    print("Unknown param")


#print("===============")
#print(filter_numbers([1, 2, 3], ODD))
#print(filter_numbers([2, 3, 4, 5], EVEN))
#print("===============")
#print(filter_numbers([0,1,2,3,4,5,6,7,8,9,10,11], PRIME))
