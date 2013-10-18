def prime_factors(n):
    factors = []
    lastresult = n

    # 1 is a special case
    if n == 1:
        return [1]

    while 1:
        if lastresult == 1:
            break

        c = 2

        while 1:
            if lastresult % c == 0:
                break

            c += 1
        if c not in factors:
            factors.append(c)
        lastresult /= c

    return factors

def gcd(a, b):
    if a == 0:
        return b

    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
