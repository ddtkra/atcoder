#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, S: int):
    return

    def combination(n, r, mod=10**9+7):
        n1, r = n+1, min(r, n-r)
        numer = denom = 1
        for i in range(1, r+1):
            numer = numer * (n1-i) % mod
            denom = denom * i % mod
        return numer * pow(denom, mod-2, mod) % mod



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(N, S)

if __name__ == '__main__':
    main()
