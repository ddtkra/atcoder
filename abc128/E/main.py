#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, Q: int, S: "List[int]", T: "List[int]", X: "List[int]", D: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
    D = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, S, T, X, D)

if __name__ == '__main__':
    main()
