#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, X: "List[int]", Y: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (2 * N + 1)  # type: "List[int]"
    Y = [int()] * (2 * N + 1)  # type: "List[int]"
    for i in range(2 * N + 1):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)

if __name__ == '__main__':
    main()
