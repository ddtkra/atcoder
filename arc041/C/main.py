#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, L: int, x: "List[int]", d: "List[str]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    d = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = int(next(tokens))
        d[i] = next(tokens)
    solve(N, L, x, d)

if __name__ == '__main__':
    main()
