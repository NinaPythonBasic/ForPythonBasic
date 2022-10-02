"""
Домашнее задание №1
Функции и структуры данных
"""
import math

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
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            prime_flag = False
            break
    return prime_flag

def filter_numbers(nums, param):
    if (param == ODD):
        return list(filter(lambda x: x % 2 != 0, nums))
    elif (param == EVEN):
        return list(filter(lambda x: x % 2 == 0, nums))
    elif (param == PRIME):
        return list(filter(is_prime, nums))
    print("Unknown param")

