#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(T: int, N: int, P: float, q: "List[float]", x: "List[int]", t: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    P = float(next(tokens))  # type: float
    q = [float()] * (N)  # type: "List[float]"
    x = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        q[i] = float(next(tokens))
        x[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(T, N, P, q, x, t)

if __name__ == '__main__':
    main()
