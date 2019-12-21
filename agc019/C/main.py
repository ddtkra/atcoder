#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(x: "List[int]", y: "List[int]", N: int, X: "List[int]", Y: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int()] * (2)  # type: "List[int]"
    y = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(x, y, N, X, Y)

if __name__ == '__main__':
    main()
