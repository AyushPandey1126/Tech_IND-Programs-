# Q1 1. Factorial 

def factorial(n):
    if n == 0 or n == 1 : 
        return 1 
    return n * factorial(n-1)

print(factorial(5)) # 120


# Q2 . Sum of lists in recursion

def sum_of_list(lst):
    if lst == [] :
        return 0
    return lst[0] + sum_of_list(lst[1:])

print(sum_of_list([6,3,5,3,5]))





