#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, M: int, X: "List[int]", Y: "List[int]", Q: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, X, Y, Q, A, B, C)

if __name__ == '__main__':
    main()
