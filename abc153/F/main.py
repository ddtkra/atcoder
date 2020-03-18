#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    H = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        H[i] = int(next(tokens))
    solve(N, D, A, X, H)

if __name__ == '__main__':
    main()
