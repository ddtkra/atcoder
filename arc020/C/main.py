#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", L: "List[int]", B: int):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        L[i] = int(next(tokens))
    B = int(next(tokens))  # type: int
    solve(N, a, L, B)

if __name__ == '__main__':
    main()
