# N = 10
# x = [[0] * (N) for i in range(N)]

# import itertools
# x2 = itertools.chain.from_iterable(x)

# x = sorted(x, key=lambda x:(x[0],x[1]))

def gcd(a: int, b: int):
    while b:
        a, b = b, a%b
    return a

print(gcd(6,24))

def lcm(a: int, b:int):
    return a*b // gcd(a,b)

print(lcm(3,4))


def isPrime(x :int):
    if(x == 1):
        return False
    for i in range(2, int(x**0.5)+1):
        if(x%i == 0):
            return False
    return True

print(isPrime(3))

def eratos(n :int):
    isPrimeList = [True] * (n+1)
    isPrimeList[0] = isPrimeList[1] = False
    
    for i in range(2, int(n**0.5+1)):
        if(isPrimeList[i]):
            j = i+i
            while(j <= n):
                isPrimeList[j] = False
                j = j+i
                
    return isPrimeList

for i,v in enumerate(eratos(20)):
    print(i,v)


def primeFactorize(n: int):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

print(primeFactorize(10))