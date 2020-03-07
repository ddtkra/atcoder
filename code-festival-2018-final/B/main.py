#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, r: "List[int]"):
    from math import log10, ceil
    fact = [.0] * (max(N, M)+2)
    for i in range(1, (max(N, M)+2)):
        fact[i] = log10(i)+fact[i-1]

    p = fact[N] - N*log10(M) - sum([fact[ri] for ri in r])

    print(ceil(-p))

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    r = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, r)

if __name__ == '__main__':
    main()
