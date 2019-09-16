#!/usr/bin/env python3
import sys


MOD = 1000000007  # type: int

def prime_factorize(n):
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


def solve(N: int):
    from functools import reduce
    from operator import mul

    nn = reduce(mul, range(1,N+1))
    from collections import defaultdict
    

    d = defaultdict(int)
    for i in range(2, N+1):
        t = prime_factorize(i)        

        for j in t:
            d[j] += 1

    ans = 1
    for i,v in d.items():
        if(i == 1): continue
        ans *= (v+1)

    print(ans%MOD)

    return


# Generated by 1.1.5 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
