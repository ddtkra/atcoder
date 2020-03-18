#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int):
    def isPrime(x :int):
        if(x == 1):
            return False
        for i in range(2, int(x**0.5)+1):
            if(x%i == 0):
                return False
        return True

    def divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        return divisors

    s = int(str(N)[-1])
    su = int(sum(map(int, list(str(N)))))
    # print(su)

    l = divisors(N)

    if isPrime(N):
        print("Prime")

    elif len(l) >= 2:
        if s%2 != 0 and s != 5 and su%3 != 0:
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
