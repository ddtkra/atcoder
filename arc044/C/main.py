#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(W: int, H: int, Q: int, T: "List[int]", D: "List[int]", X: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    T = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        D[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(W, H, Q, T, D, X)

if __name__ == '__main__':
    main()
