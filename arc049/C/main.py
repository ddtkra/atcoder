#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, A: int, x: "List[int]", y: "List[int]", B: int, u: "List[int]", v: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    x = [int()] * (A)  # type: "List[int]"
    y = [int()] * (A)  # type: "List[int]"
    for i in range(A):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    B = int(next(tokens))  # type: int
    u = [int()] * (B)  # type: "List[int]"
    v = [int()] * (B)  # type: "List[int]"
    for i in range(B):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, A, x, y, B, u, v)

if __name__ == '__main__':
    main()
