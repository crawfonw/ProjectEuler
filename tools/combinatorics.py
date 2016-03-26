from math import factorial

def number_permutations(n,k):
    return factorial(n) // factorial(n-k)

def number_combinations(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))
